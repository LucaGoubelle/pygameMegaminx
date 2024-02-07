""" megaminx drawer """
import pygame

class MegaminxDrawer:
    """ megaminx drawer """
    dim3d = {
        "body": [
            (248,68),(133,100),(68,193),(62,311),(134,400),(247,442),(356,399),(429,305),(420,195),(363,104)
        ],
        "up":[
            [(248,70), (285,82), (253,91), (244,91), (211,81)],
            [(297,84), (303,86), (290,104), (262,95)],
            [(312,89), (353,103), (341,122), (301,107), (301,104)],
            [(292,112), (298,112), (333,122), (333,126), (288,127), (284,126)],
            [(284,131), (329,132), (317,151), (266,151), (276,134)],
            [(263,129), (265,132), (253,150), (244,150), (230,132), (232,129)],
            [(210,130), (219,134), (232,149), (181,151), (165,130)],
            [(197,112), (209,123), (205,126), (161,126), (159,122), (192,113)],
            [(179,89), (194,103), (194,106), (162,117), (156,117), (142,99)],
            [(198,84), (231,93), (232,96), (213,102), (204,101), (191,85)],
            [(255,100), (279,110), (279,113), (267,124), (260,126), (232,126), (221,123), (210,111), (236,100)]
        ],
        "front":[
            [(179,163), (228,162), (230,167), (218,203), (207,212), (167,212), (164,208)],
            [(244,163), (251,163), (266,205), (261,211), (234,211), (228,206)],
            [(268,163), (316,163), (332,209), (328,212), (288,212), (276,203), (264,168)],
            [(290,223), (332,223), (338,230), (297,258), (291,253), (284,228)],
            [(333,245), (337,245), (355,290), (317,320), (311,319), (298,282), (301,270)],
            [(282,282), (289,286), (303,328), (296,334), (257,307), (257,298)],
            [(238,312), (249,312), (283,335), (283,340), (243,369), (203,342), (203,337)],
            [(208,280), (230,296), (229,304), (192,331), (185,326), (200,281)],
            [(148,243), (153,243), (186,266), (189,280), (176,316), (169,316), (134,289), (134,285)],
            [(156,221), (203,221), (208,226), (197,257), (190,257), (154,230)],
            [(232,221), (260,221), (273,232), (281,257), (279,270), (250,290), (238,290), (210,266), (209,254), (220,228)],
        ],
        "left":[
            [(131,108), (144,125), (119,158), (107,142)],
            [(147,132), (149,134), (133,178), (124,168), (124,163)],
            [(153,141), (167,159), (152,205), (149,205), (139,190), (139,180)],
            [(131,200), (134,200), (146,217), (143,225), (121,232), (121,226)],
            [(136,237), (136,241), (122,284), (100,292), (101,286), (112,252), (118,244)],
            [(106,249), (107,253), (95,289), (90,294), (91,258), (93,253)],
            [(82,255), (86,258), (85,290), (81,296), (64,301), (66,262)],
            [(85,216), (88,216), (87,238), (82,245), (66,250), (67,243)],
            [(91,164), (90,196), (85,207), (68,231), (70,195)],
            [(102,150), (112,164), (111,171), (97,189), (98,155)],
            [(114,178), (118,178), (125,188), (124,201), (116,226), (109,236), (99,240), (94,236), (95,209), (100,196)]
        ],
        "right":[
            [(340,140), (356,183), (356,190), (345,207), (327,161)],
            [(346,132), (369,165), (369,169), (361,179), (344,134)],
            [(366,112), (386,143), (386,147), (376,162), (355,132), (355,128)],
            [(392,154), (396,161), (397,195), (394,195), (383,178), (383,169)],
            [(399,166), (418,196), (421,234), (404,209), (400,196)],
            [(403,214), (423,242), (423,248), (407,242), (402,234), (401,216)],
            [(406,251), (423,256), (427,297), (409,293), (405,288), (403,254)],
            [(383,249), (394,252), (398,258), (399,295), (396,295), (381,254)],
            [(353,240), (369,245), (376,253), (388,286), (388,293), (366,287), (350,243)],
            [(359,201), (370,228), (370,234), (352,228), (346,220)],
            [(372,179), (376,179), (392,202), (396,215), (396,237), (392,241), (383,239), (377,233), (365,200), (365,190)]    
        ],
        "downLeft":[
            [(127,299), (167,328), (151,335), (146,335), (105,307)],
            [(178,335), (186,340), (187,361), (182,361), (159,345), (158,341)],
            [(194,350), (232,375), (236,379), (236,400), (202,377), (195,368)],
            [(200,381), (237,407), (237,411), (203,398), (198,393), (197,382)],
            [(203,402), (235,414), (239,418), (239,436), (200,420), (199,404)],
            [(163,387), (184,396), (189,402), (189,418), (183,416), (161,390)],
            [(112,368), (141,379), (153,387), (172,411), (136,398)],
            [(116,350), (122,352), (138,373), (107,361), (101,355)],
            [(89,309), (112,338), (112,342), (98,347), (93,346), (69,316)],
            [(99,307), (134,333), (136,337), (124,341), (118,337), (95,309)],
            [(143,345), (151,346), (182,368), (188,376), (188,386), (183,389), (158,380), (149,373), (133,354), (133,348)]
        ],
        "downRight":[
            [(360,301), (382,306), (382,308), (345,334), (336,335), (321,331)],
            [(389,309), (392,310), (367,340), (353,338), (353,335)],
            [(400,306), (422,310), (397,342), (379,339), (379,334)],
            [(371,347), (390,351), (387,356), (357,369), (354,366), (367,350)],
            [(379,365), (356,394), (322,409), (340,385), (350,377)],
            [(329,387), (329,391), (307,416), (302,416), (302,399), (308,395)],
            [(287,402), (294,404), (294,417), (290,422), (257,436), (253,433), (253,416)],
            [(288,380), (293,380), (293,392), (287,397), (252,410), (252,407)],
            [(287,351), (292,351), (292,368), (286,375), (255,399), (251,399), (250,379)],
            [(308,339), (329,342), (329,346), (308,362), (302,362), (303,343)],
            [(342,346), (354,348), (357,354), (343,371), (330,380), (312,387), (302,387), (302,376), (310,366), (331,350)]
        ]
    }
    
    def __init__(self):
        pass
    
    def draw(self, scr, minx):
        """ draw puzzle """
        pygame.draw.polygon(scr, (0,0,0), MegaminxDrawer.dim3d["body"])
        for i in range(11):
            pygame.draw.polygon(scr, pygame.Color(minx.up[i]), MegaminxDrawer.dim3d["up"][i])
            pygame.draw.polygon(scr, pygame.Color(minx.front[i]), MegaminxDrawer.dim3d["front"][i])
            pygame.draw.polygon(scr, pygame.Color(minx.left[i]), MegaminxDrawer.dim3d["left"][i])
            pygame.draw.polygon(scr, pygame.Color(minx.right[i]), MegaminxDrawer.dim3d["right"][i])
            pygame.draw.polygon(scr, pygame.Color(minx.downLeft[i]), MegaminxDrawer.dim3d["downLeft"][i])
            pygame.draw.polygon(scr, pygame.Color(minx.downRight[i]), MegaminxDrawer.dim3d["downRight"][i])
        pygame.display.update()
