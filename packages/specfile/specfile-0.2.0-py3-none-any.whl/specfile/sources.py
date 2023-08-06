# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import collections
import re
import urllib.parse
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable, List, Optional, Tuple, Union, overload

from specfile.exceptions import SpecfileException
from specfile.rpm import Macros
from specfile.sourcelist import Sourcelist, SourcelistEntry
from specfile.tags import Comments, Tag, Tags


class Source(ABC):
    """Class that represents a source."""

    @property  # type: ignore
    @abstractmethod
    def index(self) -> int:
        """Numeric index of the source."""
        pass

    @property  # type: ignore
    @abstractmethod
    def location(self) -> str:
        """Literal location of the source as stored in the spec file."""
        pass

    @location.setter  # type: ignore
    @abstractmethod
    def location(self, value: str) -> None:
        pass

    @property  # type: ignore
    @abstractmethod
    def expanded_location(self) -> str:
        """Location of the source after expanding macros."""
        pass

    @property  # type: ignore
    @abstractmethod
    def filename(self) -> str:
        """Literal filename of the source."""
        pass

    @property  # type: ignore
    @abstractmethod
    def expanded_filename(self) -> str:
        """Filename of the source after expanding macros."""
        pass

    @property  # type: ignore
    @abstractmethod
    def comments(self) -> Comments:
        """List of comments associated with the source."""
        pass


class TagSource(Source):
    """Class that represents a source backed by a spec file tag."""

    def __init__(self, tag: Tag) -> None:
        """
        Constructs a `TagSource` object.

        Args:
            tag: Tag that this source represents.

        Returns:
            Constructed instance of `TagSource` class.
        """
        self._tag = tag

    def __repr__(self) -> str:
        tag = repr(self._tag)
        return f"TagSource({tag})"

    def _get_index(self) -> Optional[str]:
        """
        Extracts numeric index from tag name.

        Returns:
            Extracted index or None if there isn't one.
        """
        tokens = re.split(r"(\d+)", self._tag.name, maxsplit=1)
        if len(tokens) > 1:
            return tokens[1]
        return None

    @property
    def index(self) -> int:
        """Numeric index of the source."""
        return int(self._get_index() or 0)

    @property
    def index_digits(self) -> int:
        """Number of digits the index is formed by."""
        return len(self._get_index() or "")

    @property
    def location(self) -> str:
        """Literal location of the source as stored in the spec file."""
        return self._tag.value

    @location.setter
    def location(self, value: str) -> None:
        self._tag.value = value

    @property
    def expanded_location(self) -> str:
        """Location of the source after expanding macros."""
        return self._tag.expanded_value

    @property
    def filename(self) -> str:
        """Literal filename of the source."""
        return Path(urllib.parse.urlsplit(self._tag.value).path).name

    @property
    def expanded_filename(self) -> str:
        """Filename of the source after expanding macros."""
        return Path(urllib.parse.urlsplit(self._tag.expanded_value).path).name

    @property
    def comments(self) -> Comments:
        """List of comments associated with the source."""
        return self._tag.comments


class ListSource(Source):
    """Class that represents a source backed by a line in a %sourcelist/%patchlist section."""

    def __init__(self, source: SourcelistEntry, index: int) -> None:
        """
        Constructs a `ListSource` object.

        Args:
            source: Sourcelist entry that this source represents.
            index: Global index of the source.

        Returns:
            Constructed instance of `ListSource` class.
        """
        self._source = source
        self._index = index

    def __repr__(self) -> str:
        source = repr(self._source)
        return f"ListSource({source}, {self._index})"

    @property
    def index(self) -> int:
        """Numeric index of the source."""
        return self._index

    @property
    def location(self) -> str:
        """Literal location of the source as stored in the spec file."""
        return self._source.location

    @location.setter
    def location(self, value: str) -> None:
        self._source.location = value

    @property
    def expanded_location(self) -> str:
        """Location of the source after expanding macros."""
        return self._source.expanded_location

    @property
    def filename(self) -> str:
        """Literal filename of the source."""
        return Path(urllib.parse.urlsplit(self._source.location).path).name

    @property
    def expanded_filename(self) -> str:
        """Filename of the source after expanding macros."""
        return Path(urllib.parse.urlsplit(self._source.expanded_location).path).name

    @property
    def comments(self) -> Comments:
        """List of comments associated with the source."""
        return self._source.comments


class Sources(collections.abc.MutableSequence):
    """Class that represents a sequence of all sources."""

    PREFIX = "Source"

    def __init__(
        self, tags: Tags, sourcelists: List[Sourcelist], allow_duplicates: bool = False
    ) -> None:
        """
        Constructs a `Sources` object.

        Args:
            tags: All spec file tags.
            sourcelists: List of all %sourcelist sections.
            allow_duplicates: Whether to allow duplicate entries when adding new sources.

        Returns:
            Constructed instance of `Sources` class.
        """
        self._tags = tags
        self._sourcelists = sourcelists
        self._allow_duplicates = allow_duplicates

    def __repr__(self) -> str:
        tags = repr(self._tags)
        sourcelists = repr(self._sourcelists)
        allow_duplicates = repr(self._allow_duplicates)
        # determine class name dynamically so that inherited classes
        # don't have to reimplement __repr__()
        return f"{self.__class__.__name__}({tags}, {sourcelists}, {allow_duplicates})"

    def __contains__(self, location: object) -> bool:
        items = self._get_items()
        if not items:
            return False
        return location in [s.location for s in list(zip(*items))[0]]

    def __len__(self) -> int:
        return len(self._get_items())

    @overload
    def __getitem__(self, i: int) -> Source:
        pass

    @overload
    def __getitem__(self, i: slice) -> List[Source]:
        pass

    def __getitem__(self, i):
        items = self._get_items()
        if isinstance(i, slice):
            return list(zip(*items[i]))[0]
        else:
            return items[i][0]

    @overload
    def __setitem__(self, i: int, item: str) -> None:
        pass

    @overload
    def __setitem__(self, i: slice, item: Iterable[str]) -> None:
        pass

    def __setitem__(self, i, item):
        items = self._get_items()
        if isinstance(i, slice):
            for i0, i1 in enumerate(range(len(items))[i]):
                items[i1][0].location = item[i0]
        else:
            items[i][0].location = item

    def __delitem__(self, i: Union[int, slice]) -> None:
        items = self._get_items()
        if isinstance(i, slice):
            for _, container, index in reversed(items[i]):
                del container[index]
        else:
            _, container, index = items[i]
            del container[index]

    def _get_tags(self) -> List[Tuple[Source, Union[Tags, Sourcelist], int]]:
        """
        Gets all tag sources.

        Returns:
            List of tuples in the form of (source, container, index),
            where source is an instance of `TagSource` representing a tag,
            container is the container the tag is part of and index
            is its index within that container.
        """
        return [
            (TagSource(t), self._tags, i)
            for i, t in enumerate(self._tags)
            if t.name.capitalize().startswith(self.PREFIX.capitalize())
        ]

    def _get_items(self) -> List[Tuple[Source, Union[Tags, Sourcelist], int]]:
        """
        Gets all sources.

        Returns:
            List of tuples in the form of (source, container, index),
            where source is an instance of `TagSource` or `ListSource`
            representing a source, container is the container the source
            is part of and index is its index within that container.
        """
        result = self._get_tags()
        last_index = result[-1][0].index if result else -1
        result.extend(
            (ListSource(sl[i], last_index + 1 + i), sl, i)
            for sl in self._sourcelists
            for i in range(len(sl))
        )
        return result

    def _get_tag_format(self, reference: TagSource, index: int) -> Tuple[str, str]:
        """
        Determines name and separator of a new source tag based on
        a reference tag and the requested index.

        The new name has the same number of digits as the reference
        and the length of the separator is adjusted accordingly.

        Args:
            reference: Reference tag source.
            index: Requested index.

        Returns:
            Tuple in the form of (name, separator).
        """
        prefix = self.PREFIX.capitalize()
        name = f"{prefix}{index:0{reference.index_digits}}"
        diff = len(reference._tag.name) - len(name)
        if diff >= 0:
            return name, reference._tag._separator + " " * diff
        return name, reference._tag._separator[:diff] or ":"

    def _get_initial_tag_setup(self) -> Tuple[int, str, str]:
        """
        Determines the initial placement, name and separator of
        a new source tag. The placement is expressed as an index
        in the list of all tags.

        Returns:
            Tuple in the form of (index, name, separator).
        """
        prefix = self.PREFIX.capitalize()
        return len(self._tags) if self._tags else 0, f"{prefix}0", ": "

    def _deduplicate_tag_names(self) -> None:
        """Eliminates duplicate indexes in source tag names."""
        tags = self._get_tags()
        if not tags:
            return
        tag_sources = sorted(list(zip(*tags))[0], key=lambda ts: ts.index)
        for ts0, ts1 in zip(tag_sources, tag_sources[1:]):
            if ts1.index <= ts0.index:
                ts1._tag.name, ts1._tag._separator = self._get_tag_format(
                    ts0, ts0.index + 1
                )

    def insert(self, i: int, location: str) -> None:
        """
        Inserts a new source at a specified index.

        Args:
            i: Requested index.
            location: Location of the new source.

        Raises:
            SpecfileException if duplicates are disallowed and there
            already is a source with the same location.
        """
        if not self._allow_duplicates and location in self:
            raise SpecfileException(f"Source '{location}' already exists")
        items = self._get_items()
        if i > len(items):
            i = len(items)
        if items:
            if i == len(items):
                source, container, index = items[-1]
                index += 1
                source_index = source.index + 1
            else:
                source, container, index = items[i]
                source_index = source.index
            if isinstance(source, TagSource):
                name, separator = self._get_tag_format(source, source_index)
                container.insert(
                    index,
                    Tag(name, location, Macros.expand(location), separator, Comments()),
                )
                self._deduplicate_tag_names()
            else:
                container.insert(index, SourcelistEntry(location, Comments()))
        elif self._sourcelists:
            self._sourcelists[-1].append(SourcelistEntry(location, Comments()))
        else:
            index, name, separator = self._get_initial_tag_setup()
            self._tags.insert(
                index,
                Tag(name, location, Macros.expand(location), separator, Comments()),
            )

    def remove(self, location: str) -> None:
        """
        Removes sources by location.

        Args:
            location: Location of the sources to be removed.
        """
        for source, container, index in reversed(self._get_items()):
            if source.location == location:
                del container[index]

    def count(self, location: str) -> int:
        """
        Counts sources by location.

        Args:
            location: Location of the sources to be counted.

        Returns:
            Number of sources with the specified location.
        """
        items = self._get_items()
        if not items:
            return 0
        return len([s for s in list(zip(*items))[0] if s.location == location])


class Patches(Sources):
    """Class that represents a sequence of all patches."""

    PREFIX = "Patch"

    def _get_initial_tag_setup(self) -> Tuple[int, str, str]:
        """
        Determines the initial placement, name and separator of
        a new source tag. The placement is expressed as an index
        in the list of all tags.

        Returns:
            Tuple in the form of (index, name, separator).
        """
        try:
            index, source = [
                (i, TagSource(t))
                for i, t in enumerate(self._tags)
                if t.name.capitalize().startswith("Source")
            ][-1]
        except IndexError:
            return super()._get_initial_tag_setup()
        name, separator = self._get_tag_format(source, 0)
        return index + 1, name, separator
