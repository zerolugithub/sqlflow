
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDnonassocLELEGEGTEQNEADD ALERT ALL ALTER AND ASC CHAR CREATE DELETE DESC DROP EQ EXIT FROM GE GRANT GT HELP ID INDEX INSERT INT INTO IS KEY LE LOAD LT NE NOT NULL NUMBER ON OR PASSWORD PRIMARY PRINT REVOKE SELECT SET SHOW STRING TABLE TABLES TO UPDATE USER VALUES VIEW WHERE start : command ';'  command : ddl\n                | dml\n                | utility\n                | nothing  ddl : createtable\n            | createindex\n            | droptable\n            | dropindex\n            | showtables\n            | alerttable\n            | createuser\n            | grantuser\n            | revokeuser  dml : query\n            | insert\n            | delete\n            | update  utility : exit\n                | print  showtables : SHOW TABLES  createuser : CREATE USER ID PASSWORD STRING grantuser : GRANT power_list ON non_mrelation_list TO non_mrelation_list  revokeuser : REVOKE power_list ON non_mrelation_list FROM non_mrelation_list  power_list : power_list ',' power_type\n                   | power_type   power_type : SELECT\n                    | UPDATE\n                    | INSERT\n                    | DELETE\n                    | PRINT\n                    | ALL\n     alerttable : ALERT TABLE ID ADD attrtype\n                   | ALERT TABLE ID DROP non_mrelation_list  createtable : CREATE TABLE ID '(' non_mattrtype_list ')'  createindex : CREATE INDEX ID '(' ID ')'  droptable : DROP TABLE ID  dropindex : DROP INDEX ID '(' ID ')'  print : PRINT ID  exit : EXIT  query : SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause  insert : INSERT INTO ID VALUES inservalue_list  inservalue_list : '(' non_mvalue_list ')' ',' inservalue_list\n                        | '(' non_mvalue_list ')'  delete : DELETE FROM ID opwhere_clause  update : UPDATE ID SET relattr EQ relattr_or_value opwhere_clause  non_mattrtype_list : attrtype ',' non_mattrtype_list\n                           | attrtype  attrtype : ID type\n                 | ID type '(' NUMBER ')'\n                 | PRIMARY KEY '(' ID ')'  type : INT\n             | CHAR  non_mselect_clause : non_mrelattr_list\n                           | '*'  non_mrelattr_list : relattr ',' non_mrelattr_list\n                          | relattr  relattr : ID '.' ID\n                | ID  non_mrelation_list : relation ',' non_mrelation_list\n                           | relation  relation : ID  opwhere_clause : WHERE non_mcond_list\n                       | nothing  non_mcond_list : non_mcond_list AND non_mcond_list\n                       | non_mcond_list OR  non_mcond_list\n                       | '(' non_mcond_list ')'\n                       | condition  condition : relattr op relattr_or_value\n                  | relattr EQ null_value\n                  | relattr NE null_value  relattr_or_value : relattr\n                         | value  non_mvalue_list : value ',' non_mvalue_list\n                        | value\n                        | null_value ',' non_mvalue_list\n                        | null_value  value : STRING  value : NUMBER  null_value : NULL  op : LT\n           | LE\n           | GT\n           | GE\n           | EQ\n           | NE  nothing : "
    
_lr_action_items = {'USER':([27,],[53,]),'NULL':([106,123,124,153,155,],[138,138,138,138,138,]),'*':([32,],[56,]),',':([34,35,36,37,38,39,40,41,51,58,59,75,76,77,93,110,118,119,120,134,135,136,138,139,154,162,163,],[-28,-29,-31,-32,-26,-27,60,-30,60,73,-59,-25,94,-62,-58,142,-53,-49,-52,-78,-79,153,-80,155,160,-51,-50,]),';':([0,1,2,5,6,7,9,10,11,16,17,18,20,21,23,24,25,28,29,30,31,33,42,47,59,62,65,76,77,82,83,91,93,97,100,101,104,107,111,113,114,115,116,118,119,120,131,132,133,134,135,138,140,141,143,146,147,148,149,150,151,152,154,162,163,164,],[-87,-19,-9,-20,-16,-40,-15,-3,43,-4,-7,-11,-17,-2,-13,-8,-18,-14,-10,-5,-12,-6,-21,-39,-59,-37,-87,-61,-62,-45,-64,-87,-58,-33,-34,-68,-63,-42,-22,-41,-60,-24,-38,-53,-49,-52,-73,-87,-72,-78,-79,-80,-23,-35,-36,-67,-70,-71,-69,-65,-66,-46,-44,-51,-50,-43,]),')':([59,93,96,101,109,110,112,118,119,120,121,131,133,134,135,136,137,138,139,146,147,148,149,150,151,156,157,158,159,161,162,163,],[-59,-58,116,-68,141,-48,143,-53,-49,-52,146,-73,-72,-78,-79,-77,154,-80,-75,-67,-70,-71,-69,-65,-66,-47,162,163,-76,-74,-51,-50,]),'TO':([76,77,87,114,],[-61,-62,108,-60,]),'ALERT':([0,],[13,]),'REVOKE':([0,],[4,]),'EXIT':([0,],[7,]),'$end':([3,43,],[0,-1,]),'PRINT':([0,4,26,60,],[14,36,36,36,]),'SHOW':([0,],[8,]),'PASSWORD':([70,],[89,]),'LT':([59,93,103,],[-59,-58,122,]),'NE':([59,93,103,],[-59,-58,124,]),'VALUES':([67,],[86,]),'TABLES':([8,],[42,]),'INSERT':([0,4,26,60,],[22,35,35,35,]),'GT':([59,93,103,],[-59,-58,128,]),'.':([59,],[74,]),'WHERE':([59,65,76,77,91,93,114,131,132,133,134,135,],[-59,84,-61,-62,84,-58,-60,-73,84,-72,-78,-79,]),'STRING':([89,105,106,122,123,124,125,126,127,128,153,155,],[111,134,134,-81,-85,-86,-84,134,-82,-83,134,134,]),'GE':([59,93,103,],[-59,-58,125,]),'SET':([49,],[66,]),'LE':([59,93,103,],[-59,-58,127,]),'INTO':([22,],[50,]),'OR':([59,93,101,104,121,131,133,134,135,138,146,147,148,149,150,151,],[-59,-58,-68,130,130,-73,-72,-78,-79,-80,-67,-70,-71,-69,-65,-66,]),'NUMBER':([105,106,122,123,124,125,126,127,128,145,153,155,],[135,135,-81,-85,-86,-84,135,-82,-83,158,135,135,]),'PRIMARY':([80,88,142,],[98,98,98,]),'KEY':([98,],[117,]),'INDEX':([12,27,],[45,54,]),'ID':([14,19,32,44,45,46,48,50,52,53,54,61,66,68,72,73,74,79,80,81,84,88,90,94,95,102,105,108,122,123,124,125,126,127,128,129,130,142,144,],[47,49,59,62,63,64,65,67,69,70,71,77,59,77,77,59,93,96,99,77,59,99,112,77,77,59,59,77,-81,-85,-86,-84,59,-82,-83,59,59,99,157,]),'TABLE':([12,13,27,],[44,46,52,]),'FROM':([15,55,56,57,58,59,76,77,78,92,93,114,],[48,72,-55,-54,-57,-59,-61,-62,95,-56,-58,-60,]),'DELETE':([0,4,26,60,],[15,41,41,41,]),'ON':([34,35,36,37,38,39,40,41,51,75,],[-28,-29,-31,-32,-26,-27,61,-30,68,-25,]),'UPDATE':([0,4,26,60,],[19,34,34,34,]),'GRANT':([0,],[26,]),'EQ':([59,85,93,103,],[-59,105,-58,123,]),'CREATE':([0,],[27,]),'CHAR':([99,],[118,]),'ALL':([4,26,60,],[37,37,37,]),'ADD':([64,],[80,]),'AND':([59,93,101,104,121,131,133,134,135,138,146,147,148,149,150,151,],[-59,-58,-68,129,129,-73,-72,-78,-79,-80,-67,-70,-71,-69,-65,129,]),'DROP':([0,64,],[12,81,]),'(':([63,69,71,84,86,102,117,118,119,120,129,130,160,],[79,88,90,102,106,102,144,-53,145,-52,102,102,106,]),'SELECT':([0,4,26,60,],[32,39,39,39,]),'INT':([99,],[120,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exit':([0,],[1,]),'dropindex':([0,],[2,]),'createindex':([0,],[17,]),'relattr_or_value':([105,126,],[132,149,]),'relation':([61,68,72,81,94,95,108,],[76,76,76,76,76,76,76,]),'inservalue_list':([86,160,],[107,164,]),'delete':([0,],[20,]),'ddl':([0,],[21,]),'condition':([84,102,129,130,],[101,101,101,101,]),'start':([0,],[3,]),'opwhere_clause':([65,91,132,],[82,113,152,]),'value':([105,106,126,153,155,],[131,139,131,139,139,]),'type':([99,],[119,]),'attrtype':([80,88,142,],[97,110,110,]),'print':([0,],[5,]),'power_type':([4,26,60,],[38,38,75,]),'insert':([0,],[6,]),'op':([103,],[126,]),'grantuser':([0,],[23,]),'droptable':([0,],[24,]),'update':([0,],[25,]),'null_value':([106,123,124,153,155,],[136,147,148,136,136,]),'query':([0,],[9,]),'dml':([0,],[10,]),'command':([0,],[11,]),'power_list':([4,26,],[40,51,]),'revokeuser':([0,],[28,]),'showtables':([0,],[29,]),'non_mcond_list':([84,102,129,130,],[104,121,150,151,]),'non_mrelation_list':([61,68,72,81,94,95,108,],[78,87,91,100,114,115,140,]),'non_mselect_clause':([32,],[55,]),'nothing':([0,65,91,132,],[30,83,83,83,]),'non_mvalue_list':([106,153,155,],[137,159,161,]),'non_mrelattr_list':([32,73,],[57,92,]),'alerttable':([0,],[18,]),'createuser':([0,],[31,]),'non_mattrtype_list':([88,142,],[109,156,]),'createtable':([0,],[33,]),'utility':([0,],[16,]),'relattr':([32,66,73,84,102,105,126,129,130,],[58,85,58,103,103,133,133,103,103,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> command ;','start',2,'p_start','parser.py',20),
  ('command -> ddl','command',1,'p_command','parser.py',25),
  ('command -> dml','command',1,'p_command','parser.py',26),
  ('command -> utility','command',1,'p_command','parser.py',27),
  ('command -> nothing','command',1,'p_command','parser.py',28),
  ('ddl -> createtable','ddl',1,'p_ddl','parser.py',33),
  ('ddl -> createindex','ddl',1,'p_ddl','parser.py',34),
  ('ddl -> droptable','ddl',1,'p_ddl','parser.py',35),
  ('ddl -> dropindex','ddl',1,'p_ddl','parser.py',36),
  ('ddl -> showtables','ddl',1,'p_ddl','parser.py',37),
  ('ddl -> alerttable','ddl',1,'p_ddl','parser.py',38),
  ('ddl -> createuser','ddl',1,'p_ddl','parser.py',39),
  ('ddl -> grantuser','ddl',1,'p_ddl','parser.py',40),
  ('ddl -> revokeuser','ddl',1,'p_ddl','parser.py',41),
  ('dml -> query','dml',1,'p_dml','parser.py',46),
  ('dml -> insert','dml',1,'p_dml','parser.py',47),
  ('dml -> delete','dml',1,'p_dml','parser.py',48),
  ('dml -> update','dml',1,'p_dml','parser.py',49),
  ('utility -> exit','utility',1,'p_utility','parser.py',54),
  ('utility -> print','utility',1,'p_utility','parser.py',55),
  ('showtables -> SHOW TABLES','showtables',2,'p_showtables','parser.py',60),
  ('createuser -> CREATE USER ID PASSWORD STRING','createuser',5,'p_createuser','parser.py',65),
  ('grantuser -> GRANT power_list ON non_mrelation_list TO non_mrelation_list','grantuser',6,'p_grantuser','parser.py',70),
  ('revokeuser -> REVOKE power_list ON non_mrelation_list FROM non_mrelation_list','revokeuser',6,'p_revokeuser','parser.py',75),
  ('power_list -> power_list , power_type','power_list',3,'p_power_list','parser.py',80),
  ('power_list -> power_type','power_list',1,'p_power_list','parser.py',81),
  ('power_type -> SELECT','power_type',1,'p_power_type','parser.py',89),
  ('power_type -> UPDATE','power_type',1,'p_power_type','parser.py',90),
  ('power_type -> INSERT','power_type',1,'p_power_type','parser.py',91),
  ('power_type -> DELETE','power_type',1,'p_power_type','parser.py',92),
  ('power_type -> PRINT','power_type',1,'p_power_type','parser.py',93),
  ('power_type -> ALL','power_type',1,'p_power_type','parser.py',94),
  ('alerttable -> ALERT TABLE ID ADD attrtype','alerttable',5,'p_alerttable','parser.py',100),
  ('alerttable -> ALERT TABLE ID DROP non_mrelation_list','alerttable',5,'p_alerttable','parser.py',101),
  ('createtable -> CREATE TABLE ID ( non_mattrtype_list )','createtable',6,'p_createtable','parser.py',109),
  ('createindex -> CREATE INDEX ID ( ID )','createindex',6,'p_createindex','parser.py',114),
  ('droptable -> DROP TABLE ID','droptable',3,'p_droptable','parser.py',119),
  ('dropindex -> DROP INDEX ID ( ID )','dropindex',6,'p_dropindex','parser.py',124),
  ('print -> PRINT ID','print',2,'p_print','parser.py',129),
  ('exit -> EXIT','exit',1,'p_exit','parser.py',134),
  ('query -> SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause','query',5,'p_query','parser.py',139),
  ('insert -> INSERT INTO ID VALUES inservalue_list','insert',5,'p_insert','parser.py',144),
  ('inservalue_list -> ( non_mvalue_list ) , inservalue_list','inservalue_list',5,'p_inservalue_list','parser.py',149),
  ('inservalue_list -> ( non_mvalue_list )','inservalue_list',3,'p_inservalue_list','parser.py',150),
  ('delete -> DELETE FROM ID opwhere_clause','delete',4,'p_delete','parser.py',158),
  ('update -> UPDATE ID SET relattr EQ relattr_or_value opwhere_clause','update',7,'p_update','parser.py',163),
  ('non_mattrtype_list -> attrtype , non_mattrtype_list','non_mattrtype_list',3,'p_non_mattrtype_list','parser.py',168),
  ('non_mattrtype_list -> attrtype','non_mattrtype_list',1,'p_non_mattrtype_list','parser.py',169),
  ('attrtype -> ID type','attrtype',2,'p_attrtype','parser.py',177),
  ('attrtype -> ID type ( NUMBER )','attrtype',5,'p_attrtype','parser.py',178),
  ('attrtype -> PRIMARY KEY ( ID )','attrtype',5,'p_attrtype','parser.py',179),
  ('type -> INT','type',1,'p_type','parser.py',189),
  ('type -> CHAR','type',1,'p_type','parser.py',190),
  ('non_mselect_clause -> non_mrelattr_list','non_mselect_clause',1,'p_non_mselect_clause','parser.py',195),
  ('non_mselect_clause -> *','non_mselect_clause',1,'p_non_mselect_clause','parser.py',196),
  ('non_mrelattr_list -> relattr , non_mrelattr_list','non_mrelattr_list',3,'p_non_mrelattr_list','parser.py',201),
  ('non_mrelattr_list -> relattr','non_mrelattr_list',1,'p_non_mrelattr_list','parser.py',202),
  ('relattr -> ID . ID','relattr',3,'p_relattr','parser.py',210),
  ('relattr -> ID','relattr',1,'p_relattr','parser.py',211),
  ('non_mrelation_list -> relation , non_mrelation_list','non_mrelation_list',3,'p_non_mrelation_list','parser.py',219),
  ('non_mrelation_list -> relation','non_mrelation_list',1,'p_non_mrelation_list','parser.py',220),
  ('relation -> ID','relation',1,'p_relation','parser.py',228),
  ('opwhere_clause -> WHERE non_mcond_list','opwhere_clause',2,'p_opwhere_clause','parser.py',233),
  ('opwhere_clause -> nothing','opwhere_clause',1,'p_opwhere_clause','parser.py',234),
  ('non_mcond_list -> non_mcond_list AND non_mcond_list','non_mcond_list',3,'p_non_mcond_list','parser.py',240),
  ('non_mcond_list -> non_mcond_list OR non_mcond_list','non_mcond_list',3,'p_non_mcond_list','parser.py',241),
  ('non_mcond_list -> ( non_mcond_list )','non_mcond_list',3,'p_non_mcond_list','parser.py',242),
  ('non_mcond_list -> condition','non_mcond_list',1,'p_non_mcond_list','parser.py',243),
  ('condition -> relattr op relattr_or_value','condition',3,'p_condition','parser.py',253),
  ('condition -> relattr EQ null_value','condition',3,'p_condition','parser.py',254),
  ('condition -> relattr NE null_value','condition',3,'p_condition','parser.py',255),
  ('relattr_or_value -> relattr','relattr_or_value',1,'p_relattr_or_value','parser.py',260),
  ('relattr_or_value -> value','relattr_or_value',1,'p_relattr_or_value','parser.py',261),
  ('non_mvalue_list -> value , non_mvalue_list','non_mvalue_list',3,'p_non_mvalue_list','parser.py',266),
  ('non_mvalue_list -> value','non_mvalue_list',1,'p_non_mvalue_list','parser.py',267),
  ('non_mvalue_list -> null_value , non_mvalue_list','non_mvalue_list',3,'p_non_mvalue_list','parser.py',268),
  ('non_mvalue_list -> null_value','non_mvalue_list',1,'p_non_mvalue_list','parser.py',269),
  ('value -> STRING','value',1,'p_value_string','parser.py',277),
  ('value -> NUMBER','value',1,'p_value_number','parser.py',282),
  ('null_value -> NULL','null_value',1,'p_null_value','parser.py',287),
  ('op -> LT','op',1,'p_op','parser.py',292),
  ('op -> LE','op',1,'p_op','parser.py',293),
  ('op -> GT','op',1,'p_op','parser.py',294),
  ('op -> GE','op',1,'p_op','parser.py',295),
  ('op -> EQ','op',1,'p_op','parser.py',296),
  ('op -> NE','op',1,'p_op','parser.py',297),
  ('nothing -> <empty>','nothing',0,'p_nothing','parser.py',302),
]