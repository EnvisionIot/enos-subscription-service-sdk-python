from __future__ import absolute_import

from collections import namedtuple

TopicPartition = namedtuple("TopicPartition",
                            ["topic", "partition"])
