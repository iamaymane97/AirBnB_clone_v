{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x0C-python-almost_a_circle/models":{"items":[{"name":"__init__.py","path":"0x0C-python-almost_a_circle/models/__init__.py","contentType":"file"},{"name":"base.py","path":"0x0C-python-almost_a_circle/models/base.py","contentType":"file"},{"name":"rectangle.py","path":"0x0C-python-almost_a_circle/models/rectangle.py","contentType":"file"},{"name":"square.py","path":"0x0C-python-almost_a_circle/models/square.py","contentType":"file"}],"totalCount":4},"0x0C-python-almost_a_circle":{"items":[{"name":"models","path":"0x0C-python-almost_a_circle/models","contentType":"directory"},{"name":"tests","path":"0x0C-python-almost_a_circle/tests","contentType":"directory"},{"name":"README.md","path":"0x0C-python-almost_a_circle/README.md","contentType":"file"}],"totalCount":3},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x09-python-everything_is_object","path":"0x09-python-everything_is_object","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x0D-SQL_introduction","path":"0x0D-SQL_introduction","contentType":"directory"},{"name":"0x0E-SQL_more_queries","path":"0x0E-SQL_more_queries","contentType":"directory"},{"name":"0x0F-python-object_relational_mapping","path":"0x0F-python-object_relational_mapping","contentType":"directory"},{"name":"0x10-python-network_0","path":"0x10-python-network_0","contentType":"directory"},{"name":"0x11-python-network_1","path":"0x11-python-network_1","contentType":"directory"},{"name":"0x12-javascript-warm_up","path":"0x12-javascript-warm_up","contentType":"directory"},{"name":"0x13-javascript_objects_scopes_closures","path":"0x13-javascript_objects_scopes_closures","contentType":"directory"},{"name":"0x14-javascript-web_scraping","path":"0x14-javascript-web_scraping","contentType":"directory"},{"name":"0x15-javascript-web_jquery","path":"0x15-javascript-web_jquery","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":23}},"fileTreeProcessingTime":6.529079,"foldersToFetch":[],"repo":{"id":497984705,"defaultBranch":"main","name":"alx-higher_level_programming","ownerLogin":"Tolulope05","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2022-05-30T14:48:10.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/97342222?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1666824814.882072","canEdit":false,"refType":"branch","currentOid":"ca371a3cb0e3fd554b81fe18ec5b820add4e2f67"},"path":"0x0C-python-almost_a_circle/models/square.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","\"\"\"Defines a square class.\"\"\"","from models.rectangle import Rectangle","","","class Square(Rectangle):","    \"\"\"Represent a square.\"\"\"","","    def __init__(self, size, x=0, y=0, id=None):","        \"\"\"Initialize a new Square.","","        Args:","            size (int): The size of the new Square.","            x (int): The x coordinate of the new Square.","            y (int): The y coordinate of the new Square.","            id (int): The identity of the new Square.","        \"\"\"","        super().__init__(size, size, x, y, id)","","    @property","    def size(self):","        \"\"\"Get/set the size of the Square.\"\"\"","        return self.width","","    @size.setter","    def size(self, value):","        self.width = value","        self.height = value","","    def update(self, *args, **kwargs):","        \"\"\"Update the Square.","","        Args:","            *args (ints): New attribute values.","                - 1st argument represents id attribute","                - 2nd argument represents size attribute","                - 3rd argument represents x attribute","                - 4th argument represents y attribute","            **kwargs (dict): New key/value pairs of attributes.","        \"\"\"","        if args and len(args) != 0:","            a = 0","            for arg in args:","                if a == 0:","                    if arg is None:","                        self.__init__(self.size, self.x, self.y)","                    else:","                        self.id = arg","                elif a == 1:","                    self.size = arg","                elif a == 2:","                    self.x = arg","                elif a == 3:","                    self.y = arg","                a += 1","","        elif kwargs and len(kwargs) != 0:","            for k, v in kwargs.items():","                if k == \"id\":","                    if v is None:","                        self.__init__(self.size, self.x, self.y)","                    else:","                        self.id = v","                elif k == \"size\":","                    self.size = v","                elif k == \"x\":","                    self.x = v","                elif k == \"y\":","                    self.y = v","","    def to_dictionary(self):","        \"\"\"Return the dictionary representation of the Square.\"\"\"","        return {","            \"id\": self.id,","            \"size\": self.width,","            \"x\": self.x,","            \"y\": self.y","        }","","    def __str__(self):","        \"\"\"Return the print() and str() representation of a Square.\"\"\"","        return \"[Square] ({}) {}/{} - {}\".format(self.id, self.x, self.y,","                                                 self.width)"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":29,"cssClass":"pl-s"}],[{"start":0,"end":4,"cssClass":"pl-k"},{"start":5,"end":11,"cssClass":"pl-s1"},{"start":12,"end":21,"cssClass":"pl-s1"},{"start":22,"end":28,"cssClass":"pl-k"},{"start":29,"end":38,"cssClass":"pl-v"}],[],[],[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":12,"cssClass":"pl-v"},{"start":13,"end":22,"cssClass":"pl-v"}],[{"start":4,"end":29,"cssClass":"pl-s"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":16,"cssClass":"pl-en"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":23,"end":27,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":39,"end":41,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":42,"end":46,"cssClass":"pl-c1"}],[{"start":8,"end":35,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":51,"cssClass":"pl-s"}],[{"start":0,"end":56,"cssClass":"pl-s"}],[{"start":0,"end":56,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":16,"end":24,"cssClass":"pl-en"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-s1"},{"start":40,"end":41,"cssClass":"pl-s1"},{"start":43,"end":45,"cssClass":"pl-s1"}],[],[{"start":4,"end":13,"cssClass":"pl-en"},{"start":5,"end":13,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"}],[{"start":8,"end":45,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"}],[],[{"start":4,"end":16,"cssClass":"pl-en"},{"start":5,"end":9,"cssClass":"pl-s1"},{"start":10,"end":16,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":12,"cssClass":"pl-en"},{"start":13,"end":17,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":12,"cssClass":"pl-s1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":22,"end":27,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-en"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":22,"end":26,"cssClass":"pl-s1"},{"start":28,"end":30,"cssClass":"pl-c1"},{"start":30,"end":36,"cssClass":"pl-s1"}],[{"start":8,"end":29,"cssClass":"pl-s"}],[{"start":0,"end":0,"cssClass":"pl-s"}],[{"start":0,"end":13,"cssClass":"pl-s"}],[{"start":0,"end":47,"cssClass":"pl-s"}],[{"start":0,"end":54,"cssClass":"pl-s"}],[{"start":0,"end":56,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":53,"cssClass":"pl-s"}],[{"start":0,"end":63,"cssClass":"pl-s"}],[{"start":0,"end":11,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":15,"cssClass":"pl-s1"},{"start":16,"end":19,"cssClass":"pl-c1"},{"start":20,"end":23,"cssClass":"pl-en"},{"start":24,"end":28,"cssClass":"pl-s1"},{"start":30,"end":32,"cssClass":"pl-c1"},{"start":33,"end":34,"cssClass":"pl-c1"}],[{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":19,"cssClass":"pl-s1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":27,"cssClass":"pl-s1"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":20,"end":22,"cssClass":"pl-k"},{"start":23,"end":26,"cssClass":"pl-s1"},{"start":27,"end":29,"cssClass":"pl-c1"},{"start":30,"end":34,"cssClass":"pl-c1"}],[{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":37,"cssClass":"pl-en"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":43,"end":47,"cssClass":"pl-s1"},{"start":49,"end":53,"cssClass":"pl-s1"},{"start":54,"end":55,"cssClass":"pl-s1"},{"start":57,"end":61,"cssClass":"pl-s1"},{"start":62,"end":63,"cssClass":"pl-s1"}],[{"start":20,"end":24,"cssClass":"pl-k"}],[{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":37,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-k"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-k"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":32,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-k"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":32,"cssClass":"pl-s1"}],[{"start":16,"end":17,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":23,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-en"},{"start":28,"end":34,"cssClass":"pl-s1"},{"start":36,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-c1"}],[{"start":12,"end":15,"cssClass":"pl-k"},{"start":16,"end":17,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":30,"cssClass":"pl-s1"},{"start":31,"end":36,"cssClass":"pl-en"}],[{"start":16,"end":18,"cssClass":"pl-k"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":28,"cssClass":"pl-s"}],[{"start":20,"end":22,"cssClass":"pl-k"},{"start":23,"end":24,"cssClass":"pl-s1"},{"start":25,"end":27,"cssClass":"pl-c1"},{"start":28,"end":32,"cssClass":"pl-c1"}],[{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":37,"cssClass":"pl-en"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":43,"end":47,"cssClass":"pl-s1"},{"start":49,"end":53,"cssClass":"pl-s1"},{"start":54,"end":55,"cssClass":"pl-s1"},{"start":57,"end":61,"cssClass":"pl-s1"},{"start":62,"end":63,"cssClass":"pl-s1"}],[{"start":20,"end":24,"cssClass":"pl-k"}],[{"start":24,"end":28,"cssClass":"pl-s1"},{"start":29,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":35,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-k"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":32,"cssClass":"pl-s"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":29,"cssClass":"pl-s1"},{"start":30,"end":31,"cssClass":"pl-c1"},{"start":32,"end":33,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-k"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-s"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":30,"cssClass":"pl-s1"}],[{"start":16,"end":20,"cssClass":"pl-k"},{"start":21,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-s"}],[{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":26,"cssClass":"pl-s1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":29,"end":30,"cssClass":"pl-s1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":21,"cssClass":"pl-en"},{"start":22,"end":26,"cssClass":"pl-s1"}],[{"start":8,"end":65,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"}],[{"start":12,"end":16,"cssClass":"pl-s"},{"start":18,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-s1"}],[{"start":12,"end":18,"cssClass":"pl-s"},{"start":20,"end":24,"cssClass":"pl-s1"},{"start":25,"end":30,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-s1"}],[{"start":12,"end":15,"cssClass":"pl-s"},{"start":17,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-s1"}],[],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-en"},{"start":16,"end":20,"cssClass":"pl-s1"}],[{"start":8,"end":70,"cssClass":"pl-s"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":41,"cssClass":"pl-s"},{"start":42,"end":48,"cssClass":"pl-en"},{"start":49,"end":53,"cssClass":"pl-s1"},{"start":54,"end":56,"cssClass":"pl-s1"},{"start":58,"end":62,"cssClass":"pl-s1"},{"start":63,"end":64,"cssClass":"pl-s1"},{"start":66,"end":70,"cssClass":"pl-s1"},{"start":71,"end":72,"cssClass":"pl-s1"}],[{"start":49,"end":53,"cssClass":"pl-s1"},{"start":54,"end":59,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/Tolulope05/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/Tolulope05/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/Tolulope05/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"square.py","displayUrl":"https://github.com/Tolulope05/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/square.py?raw=true","headerInfo":{"blobSize":"2.51 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"8d01e9e","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FTolulope05%2Falx-higher_level_programming%2Fblob%2Fmain%2F0x0C-python-almost_a_circle%2Fmodels%2Fsquare.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"83","truncatedSloc":"72"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/Tolulope05/alx-higher_level_programming/discussions/new","newIssuePath":"/Tolulope05/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/Tolulope05/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/square.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","releasePath":"/Tolulope05/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false},"rawBlobUrl":"https://github.com/Tolulope05/alx-higher_level_programming/raw/main/0x0C-python-almost_a_circle/models/square.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"Tolulope05","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"Square","kind":"class","ident_start":96,"ident_end":102,"extent_start":90,"extent_end":2574,"fully_qualified_name":"Square","ident_utf16":{"start":{"line_number":5,"utf16_col":6},"end":{"line_number":5,"utf16_col":12}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":82,"utf16_col":60}}},{"name":"__init__","kind":"function","ident_start":154,"ident_end":162,"extent_start":150,"extent_end":524,"fully_qualified_name":"Square.__init__","ident_utf16":{"start":{"line_number":8,"utf16_col":8},"end":{"line_number":8,"utf16_col":16}},"extent_utf16":{"start":{"line_number":8,"utf16_col":4},"end":{"line_number":17,"utf16_col":46}}},{"name":"size","kind":"function","ident_start":548,"ident_end":552,"extent_start":544,"extent_end":631,"fully_qualified_name":"Square.size","ident_utf16":{"start":{"line_number":20,"utf16_col":8},"end":{"line_number":20,"utf16_col":12}},"extent_utf16":{"start":{"line_number":20,"utf16_col":4},"end":{"line_number":22,"utf16_col":25}}},{"name":"size","kind":"function","ident_start":658,"ident_end":662,"extent_start":654,"extent_end":731,"fully_qualified_name":"Square.size","ident_utf16":{"start":{"line_number":25,"utf16_col":8},"end":{"line_number":25,"utf16_col":12}},"extent_utf16":{"start":{"line_number":25,"utf16_col":4},"end":{"line_number":27,"utf16_col":27}}},{"name":"update","kind":"function","ident_start":741,"ident_end":747,"extent_start":737,"extent_end":2113,"fully_qualified_name":"Square.update","ident_utf16":{"start":{"line_number":29,"utf16_col":8},"end":{"line_number":29,"utf16_col":14}},"extent_utf16":{"start":{"line_number":29,"utf16_col":4},"end":{"line_number":68,"utf16_col":30}}},{"name":"to_dictionary","kind":"function","ident_start":2123,"ident_end":2136,"extent_start":2119,"extent_end":2344,"fully_qualified_name":"Square.to_dictionary","ident_utf16":{"start":{"line_number":70,"utf16_col":8},"end":{"line_number":70,"utf16_col":21}},"extent_utf16":{"start":{"line_number":70,"utf16_col":4},"end":{"line_number":77,"utf16_col":9}}},{"name":"__str__","kind":"function","ident_start":2354,"ident_end":2361,"extent_start":2350,"extent_end":2574,"fully_qualified_name":"Square.__str__","ident_utf16":{"start":{"line_number":79,"utf16_col":8},"end":{"line_number":79,"utf16_col":15}},"extent_utf16":{"start":{"line_number":79,"utf16_col":4},"end":{"line_number":82,"utf16_col":60}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/Tolulope05/alx-higher_level_programming/branches":{"post":"eSd6UfDQL81dVyIk0plf9PHFPtNy7s6zEZBi0t3i9ELpA2vu_NEOP9qw_O4Slx8pi8LpH-qS8lN8ei_-o-Ylgg"},"/repos/preferences":{"post":"uOepmHIl_GEd2CfebV9bQUHwSoBoolOoSlSCImy5sitAJzxFVfEjyZlsthDzPhHjfIzROWUnkdFmMORoc7ZpPQ"}}},"title":"alx-higher_level_programming/0x0C-python-almost_a_circle/models/square.py at main · Tolulope05/alx-higher_level_programming"}