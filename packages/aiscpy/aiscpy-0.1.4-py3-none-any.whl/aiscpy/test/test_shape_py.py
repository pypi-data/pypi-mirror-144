from aiscpy.shape import Shape

def test_nameTable():
    s1 = Shape('W','W44X335')
    assert s1.table == '`W-M-S-HP_shapes_AISC`'

def test_init():
    s1 = Shape("W",'W44X335')
    
    assert s1.query.queryToList == ["W","W44X335",98.5,44,1.03,15.9,1.77,2.56,2.625,1.3125,38.75,5.5,335,4.5,38.0,31100,1410,17.8,1620,1200,150,3.49,236,4.24,42.3,74.7,535000,168,1180,278,805]
    
    assert s1.query.toDict() == {'A': 98.5,'Cw': 535000, 'Ix': 31100,'Iy': 1200, 'J': 74.7, 'Qf': 278, 'Qw': 805, 'Shape': 'W44X335','Sw': 1180,  'Sx': 1410,  'Sy': 150,  'T': 38.75,  'Type': 'W',  'Wno': 168,  'Zx': 1620,  'Zy': 236,  'bf': 15.9,  'bf/(2*tf)': 4.5, 'd': 44,  'gage': 5.5,  'h/tw': 38.0,  'ho': 42.3,  'k(des)': 2.56,  'k(det)': 2.625,  'k1': 1.3125,  'rts': 4.24,  'rx': 17.8,  'ry': 3.49,  'tf': 1.77,  'tw': 1.03,  'wt./ft.': 335}
    
    assert s1.query.toDict()['Shape'] == 'W44X335'