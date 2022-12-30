
# /home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser_tables.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '4\xa4a\x00\xea\xcdZp5\xc6@\xa5\xfa\x1dCA'
    
_lr_action_items = {'NONE_TOK':([8,12,24,26,],[11,11,11,11,]),'LP_TOK':([5,8,12,24,26,],[8,12,12,12,12,]),'STRING_TOK':([8,12,24,26,],[13,13,13,13,]),'RP_TOK':([8,11,12,13,14,16,17,18,19,20,22,23,26,27,28,29,],[15,-8,22,-14,-13,25,-17,-15,-16,-19,-18,-9,-10,29,-20,-21,]),',':([11,13,14,16,17,18,19,20,22,23,28,29,],[-8,-14,-13,24,-17,-15,-16,-19,-18,26,-20,-21,]),'NUMBER_TOK':([8,12,24,26,],[14,14,14,14,]),'NL_TOK':([0,6,7,15,21,25,],[3,10,-4,-6,-5,-7,]),'TRUE_TOK':([8,12,24,26,],[17,17,17,17,]),'IDENTIFIER_TOK':([0,1,3,8,10,12,24,26,],[-11,5,-12,18,5,18,18,18,]),'FALSE_TOK':([8,12,24,26,],[19,19,19,19,]),'$end':([0,1,2,3,4,6,7,9,10,15,21,25,],[-11,-2,0,-12,-1,-11,-4,-3,-12,-6,-5,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'facts_opt':([1,],[4,]),'nl_opt':([0,6,],[1,9,]),'comma_opt':([23,],[27,]),'data_list':([8,12,],[16,23,]),'file':([0,],[2,]),'facts':([1,],[6,]),'data':([8,12,24,26,],[20,20,28,28,]),'fact':([1,10,],[7,21,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> nl_opt facts_opt','file',2,'p_file','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',36),
  ('facts_opt -> <empty>','facts_opt',0,'p_file','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',37),
  ('facts_opt -> facts nl_opt','facts_opt',2,'p_file','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',38),
  ('facts -> fact','facts',1,'p_file','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',39),
  ('facts -> facts NL_TOK fact','facts',3,'p_file','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',40),
  ('fact -> IDENTIFIER_TOK LP_TOK RP_TOK','fact',3,'p_fact0','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',45),
  ('fact -> IDENTIFIER_TOK LP_TOK data_list RP_TOK','fact',4,'p_fact1','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',49),
  ('data -> NONE_TOK','data',1,'p_none','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',53),
  ('comma_opt -> <empty>','comma_opt',0,'p_none','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',54),
  ('comma_opt -> ,','comma_opt',1,'p_none','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',55),
  ('nl_opt -> <empty>','nl_opt',0,'p_none','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',56),
  ('nl_opt -> NL_TOK','nl_opt',1,'p_none','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',57),
  ('data -> NUMBER_TOK','data',1,'p_number','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',62),
  ('data -> STRING_TOK','data',1,'p_string','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',67),
  ('data -> IDENTIFIER_TOK','data',1,'p_quoted_last','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',72),
  ('data -> FALSE_TOK','data',1,'p_false','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',77),
  ('data -> TRUE_TOK','data',1,'p_true','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',82),
  ('data -> LP_TOK RP_TOK','data',2,'p_empty_tuple','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',87),
  ('data_list -> data','data_list',1,'p_start_list','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',92),
  ('data_list -> data_list , data','data_list',3,'p_append_list','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',97),
  ('data -> LP_TOK data_list comma_opt RP_TOK','data',4,'p_tuple','/home/bruce/python/workareas/pyke-hg/r1_working/pyke/krb_compiler/kfbparser.py',103),
]
