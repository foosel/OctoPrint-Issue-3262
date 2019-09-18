# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import octoprint.plugin

class Issue3262Plugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			js=["js/issue_3262.js"]
		)

__plugin_name__ = "Issue 3262"
__plugin_author__ = "Gina Häußge"

__plugin_implementation__ = Issue3262Plugin()
