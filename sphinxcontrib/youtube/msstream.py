#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import utils


class msstream(utils.video):
    pass


class Msstream(utils.Video):
    _node = msstream


def visit_msstream_node(self, node):
    return utils.visit_video_node(self, node, platform_url="https://web.microsoftstream.com/embed/video/")


def visit_msstream_node_latex(self, node):
    return utils.visit_video_node_latex(self, node, platform="msstream", platform_url="https://web.microsoftstream.com/video/")


def unsupported_visit_msstream(self, node):
    return utils.unsupported_visit_video(self, node, platform="msstream")


_NODE_VISITORS = {
    'html': (visit_msstream_node, utils.depart_video_node),
    'latex': (visit_msstream_node_latex, utils.depart_video_node),
    'man': (unsupported_visit_msstream, None),
    'texinfo': (unsupported_visit_msstream, None),
    'text': (unsupported_visit_msstream, None)
}
