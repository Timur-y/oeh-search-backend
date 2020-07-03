# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NodeRemote(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'node': 'Node',
        'remote': 'Node'
    }

    attribute_map = {
        'node': 'node',
        'remote': 'remote'
    }

    def __init__(self, node=None, remote=None):  # noqa: E501
        """NodeRemote - a model defined in Swagger"""  # noqa: E501

        self._node = None
        self._remote = None
        self.discriminator = None

        self.node = node
        self.remote = remote

    @property
    def node(self):
        """Gets the node of this NodeRemote.  # noqa: E501


        :return: The node of this NodeRemote.  # noqa: E501
        :rtype: Node
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this NodeRemote.


        :param node: The node of this NodeRemote.  # noqa: E501
        :type: Node
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def remote(self):
        """Gets the remote of this NodeRemote.  # noqa: E501


        :return: The remote of this NodeRemote.  # noqa: E501
        :rtype: Node
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this NodeRemote.


        :param remote: The remote of this NodeRemote.  # noqa: E501
        :type: Node
        """
        if remote is None:
            raise ValueError("Invalid value for `remote`, must not be `None`")  # noqa: E501

        self._remote = remote

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NodeRemote, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeRemote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other