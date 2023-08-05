# encoding: utf-8

"""
Test data for relationship-related unit tests.
"""

from __future__ import absolute_import

from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.opc.rel import Relationships

from docx.opc.constants import NAMESPACE as NS
from docx.opc.oxml import parse_xml


class BaseBuilder(object):
    """
    Provides common behavior for all data builders.
    """
    @property
    def element(self):
        """Return element based on XML generated by builder"""
        return parse_xml(self.xml)

    def with_indent(self, indent):
        """Add integer *indent* spaces at beginning of element XML"""
        self._indent = indent
        return self


class RelationshipsBuilder(object):
    """Builder class for test Relationships"""
    partname_tmpls = {
        RT.SLIDE_MASTER: '/ppt/slideMasters/slideMaster%d.xml',
        RT.SLIDE:        '/ppt/slides/slide%d.xml',
    }

    def __init__(self):
        self.relationships = []
        self.next_rel_num = 1
        self.next_partnums = {}

    def _next_partnum(self, reltype):
        if reltype not in self.next_partnums:
            self.next_partnums[reltype] = 1
        partnum = self.next_partnums[reltype]
        self.next_partnums[reltype] = partnum + 1
        return partnum

    @property
    def next_rId(self):
        rId = 'rId%d' % self.next_rel_num
        self.next_rel_num += 1
        return rId

    def _next_tuple_partname(self, reltype):
        partname_tmpl = self.partname_tmpls[reltype]
        partnum = self._next_partnum(reltype)
        return partname_tmpl % partnum

    def build(self):
        rels = Relationships()
        for rel in self.relationships:
            rels.add_rel(rel)
        return rels


class CT_DefaultBuilder(BaseBuilder):
    """
    Test data builder for CT_Default (Default) XML element that appears in
    `[Content_Types].xml`.
    """
    def __init__(self):
        """Establish instance variables with default values"""
        self._content_type = 'application/xml'
        self._extension = 'xml'
        self._indent = 0
        self._namespace = ' xmlns="%s"' % NS.OPC_CONTENT_TYPES

    def with_content_type(self, content_type):
        """Set ContentType attribute to *content_type*"""
        self._content_type = content_type
        return self

    def with_extension(self, extension):
        """Set Extension attribute to *extension*"""
        self._extension = extension
        return self

    def without_namespace(self):
        """Don't include an 'xmlns=' attribute"""
        self._namespace = ''
        return self

    @property
    def xml(self):
        """Return Default element"""
        tmpl = '%s<Default%s Extension="%s" ContentType="%s"/>\n'
        indent = ' ' * self._indent
        return tmpl % (indent, self._namespace, self._extension,
                       self._content_type)


class CT_OverrideBuilder(BaseBuilder):
    """
    Test data builder for CT_Override (Override) XML element that appears in
    `[Content_Types].xml`.
    """
    def __init__(self):
        """Establish instance variables with default values"""
        self._content_type = 'app/vnd.type'
        self._indent = 0
        self._namespace = ' xmlns="%s"' % NS.OPC_CONTENT_TYPES
        self._partname = '/part/name.xml'

    def with_content_type(self, content_type):
        """Set ContentType attribute to *content_type*"""
        self._content_type = content_type
        return self

    def with_partname(self, partname):
        """Set PartName attribute to *partname*"""
        self._partname = partname
        return self

    def without_namespace(self):
        """Don't include an 'xmlns=' attribute"""
        self._namespace = ''
        return self

    @property
    def xml(self):
        """Return Override element"""
        tmpl = '%s<Override%s PartName="%s" ContentType="%s"/>\n'
        indent = ' ' * self._indent
        return tmpl % (indent, self._namespace, self._partname,
                       self._content_type)


class CT_RelationshipBuilder(BaseBuilder):
    """
    Test data builder for CT_Relationship (Relationship) XML element that
    appears in .rels files
    """
    def __init__(self):
        """Establish instance variables with default values"""
        self._rId = 'rId9'
        self._reltype = 'ReLtYpE'
        self._target = 'docProps/core.xml'
        self._target_mode = None
        self._indent = 0
        self._namespace = ' xmlns="%s"' % NS.OPC_RELATIONSHIPS

    def with_rId(self, rId):
        """Set Id attribute to *rId*"""
        self._rId = rId
        return self

    def with_reltype(self, reltype):
        """Set Type attribute to *reltype*"""
        self._reltype = reltype
        return self

    def with_target(self, target):
        """Set XXX attribute to *target*"""
        self._target = target
        return self

    def with_target_mode(self, target_mode):
        """Set TargetMode attribute to *target_mode*"""
        self._target_mode = None if target_mode == 'Internal' else target_mode
        return self

    def without_namespace(self):
        """Don't include an 'xmlns=' attribute"""
        self._namespace = ''
        return self

    @property
    def target_mode(self):
        if self._target_mode is None:
            return ''
        return ' TargetMode="%s"' % self._target_mode

    @property
    def xml(self):
        """Return Relationship element"""
        tmpl = '%s<Relationship%s Id="%s" Type="%s" Target="%s"%s/>\n'
        indent = ' ' * self._indent
        return tmpl % (indent, self._namespace, self._rId, self._reltype,
                       self._target, self.target_mode)


class CT_RelationshipsBuilder(BaseBuilder):
    """
    Test data builder for CT_Relationships (Relationships) XML element, the
    root element in .rels files.
    """
    def __init__(self):
        """Establish instance variables with default values"""
        self._rels = (
            ('rId1', 'http://reltype1', 'docProps/core.xml',    'Internal'),
            ('rId2', 'http://linktype', 'http://some/link',     'External'),
            ('rId3', 'http://reltype2', '../slides/slide1.xml', 'Internal'),
        )

    @property
    def xml(self):
        """
        Return XML string based on settings accumulated via method calls.
        """
        xml = '<Relationships xmlns="%s">\n' % NS.OPC_RELATIONSHIPS
        for rId, reltype, target, target_mode in self._rels:
            xml += (a_Relationship().with_rId(rId)
                                    .with_reltype(reltype)
                                    .with_target(target)
                                    .with_target_mode(target_mode)
                                    .with_indent(2)
                                    .without_namespace()
                                    .xml)
        xml += '</Relationships>\n'
        return xml


class CT_TypesBuilder(BaseBuilder):
    """
    Test data builder for CT_Types (<Types>) XML element, the root element in
    [Content_Types].xml files
    """
    def __init__(self):
        """Establish instance variables with default values"""
        self._defaults = (
            ('xml', 'application/xml'),
            ('jpeg', 'image/jpeg'),
        )
        self._empty = False
        self._overrides = (
            ('/docProps/core.xml', 'app/vnd.type1'),
            ('/ppt/presentation.xml', 'app/vnd.type2'),
            ('/docProps/thumbnail.jpeg', 'image/jpeg'),
        )

    def empty(self):
        self._empty = True
        return self

    @property
    def xml(self):
        """
        Return XML string based on settings accumulated via method calls
        """
        if self._empty:
            return '<Types xmlns="%s"/>\n' % NS.OPC_CONTENT_TYPES

        xml = '<Types xmlns="%s">\n' % NS.OPC_CONTENT_TYPES
        for extension, content_type in self._defaults:
            xml += (a_Default().with_extension(extension)
                               .with_content_type(content_type)
                               .with_indent(2)
                               .without_namespace()
                               .xml)
        for partname, content_type in self._overrides:
            xml += (an_Override().with_partname(partname)
                                 .with_content_type(content_type)
                                 .with_indent(2)
                                 .without_namespace()
                                 .xml)
        xml += '</Types>\n'
        return xml


def a_Default():
    return CT_DefaultBuilder()


def a_Relationship():
    return CT_RelationshipBuilder()


def a_Relationships():
    return CT_RelationshipsBuilder()


def a_Types():
    return CT_TypesBuilder()


def an_Override():
    return CT_OverrideBuilder()
