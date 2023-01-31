# bc_system_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def has_related_cat_cat(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'relation_cat_cat', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_related_cat_cat: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_related_cat_cat_two(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'relation_cat_cat', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_related_cat_cat_two: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_related_category(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'category_name', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_related_category: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    "True"):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_symptom_tumor(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'tumor_sintomas', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_symptom_tumor: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    "presentar"):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_symptom_organ_cat_term(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_related', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_symptom_organ_cat_term: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_symptom', context,
                              (rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_system.has_symptom_organ_cat_term: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_related_name_category(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'category', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_related_name_category: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    "Pertenece"):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_recurrent_alias_o(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'type_alias', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_recurrent_alias_o: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_alias', context,
                              (rule.pattern(1),
                               rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_system.has_recurrent_alias_o: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_recurrent_alias_no(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_alias', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_recurrent_alias_no: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                   context.lookup_data('old_category')):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_recurrent_rel_o(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'type_relationship', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_recurrent_rel_o: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_related', context,
                              (rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "bc_system.has_recurrent_rel_o: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_recurrent_rel_no(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_related', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_recurrent_rel_no: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                   context.lookup_data('old_relationship')):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_recurrent_term_no(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('system', 'type_terms', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_recurrent_term_no: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def has_recurrent_term_ca(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_category', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "bc_system.has_recurrent_term_ca: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(3).match_data(context, context,
                   context.lookup_data('name')):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('bc_system')
  
  bc_rule.bc_rule('has_related_cat_cat', This_rule_base, 'has_related',
                  has_related_cat_cat, None,
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_related_cat_cat_two', This_rule_base, 'has_related',
                  has_related_cat_cat_two, None,
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('category2'),
                   contexts.variable('category1'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_related_category', This_rule_base, 'has_alias',
                  has_related_category, None,
                  (contexts.variable('category'),
                   contexts.variable('alias'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('category'),
                   contexts.variable('alias'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_symptom_tumor', This_rule_base, 'has_symptom',
                  has_symptom_tumor, None,
                  (contexts.variable('tumor'),
                   contexts.variable('symptom'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('tumor'),
                   contexts.variable('symptom'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_symptom_organ_cat_term', This_rule_base, 'has_cat_cat_rel',
                  has_symptom_organ_cat_term, None,
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('instance1'),
                   contexts.variable('instance2'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('relationship'),
                   contexts.variable('instance1'),
                   contexts.variable('instance2'),))
  
  bc_rule.bc_rule('has_related_name_category', This_rule_base, 'has_category',
                  has_related_name_category, None,
                  (contexts.variable('name'),
                   contexts.variable('category'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('name'),
                   contexts.variable('category'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_recurrent_alias_o', This_rule_base, 'has_recurrent_alias',
                  has_recurrent_alias_o, None,
                  (contexts.variable('old_category'),
                   contexts.variable('category'),
                   contexts.variable('alias'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('old_category'),
                   contexts.variable('category'),
                   contexts.variable('alias'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_recurrent_alias_no', This_rule_base, 'has_recurrent_alias',
                  has_recurrent_alias_no, None,
                  (contexts.variable('old_category'),
                   contexts.variable('category'),
                   contexts.variable('alias'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('old_category'),
                   contexts.variable('alias'),
                   contexts.variable('relationship'),
                   contexts.variable('category'),))
  
  bc_rule.bc_rule('has_recurrent_rel_o', This_rule_base, 'has_recurrent_rel',
                  has_recurrent_rel_o, None,
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('old_relationship'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('old_relationship'),
                   contexts.variable('relationship'),
                   contexts.variable('category1'),
                   contexts.variable('category2'),))
  
  bc_rule.bc_rule('has_recurrent_rel_no', This_rule_base, 'has_recurrent_rel',
                  has_recurrent_rel_no, None,
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('old_relationship'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('category1'),
                   contexts.variable('category2'),
                   contexts.variable('old_relationship'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_recurrent_term_no', This_rule_base, 'has_recurrent_term',
                  has_recurrent_term_no, None,
                  (contexts.variable('name'),
                   contexts.variable('term'),),
                  (),
                  (contexts.variable('name'),
                   contexts.variable('term'),))
  
  bc_rule.bc_rule('has_recurrent_term_ca', This_rule_base, 'has_recurrent_term',
                  has_recurrent_term_ca, None,
                  (contexts.variable('name'),
                   contexts.variable('term'),),
                  (),
                  (contexts.variable('name'),
                   contexts.variable('category'),
                   contexts.variable('relationship'),
                   contexts.variable('term'),))


Krb_filename = '../examples/system/bc_system.krb'
Krb_lineno_map = (
    ((14, 18), (3, 3)),
    ((20, 27), (5, 5)),
    ((40, 44), (10, 10)),
    ((46, 53), (12, 12)),
    ((66, 70), (17, 17)),
    ((72, 78), (19, 19)),
    ((81, 81), (20, 20)),
    ((97, 101), (35, 35)),
    ((103, 109), (37, 37)),
    ((112, 112), (38, 38)),
    ((128, 132), (84, 84)),
    ((134, 141), (86, 86)),
    ((142, 149), (87, 87)),
    ((162, 166), (91, 91)),
    ((168, 174), (93, 93)),
    ((177, 177), (94, 94)),
    ((193, 197), (100, 100)),
    ((199, 205), (102, 102)),
    ((206, 213), (103, 103)),
    ((226, 230), (106, 106)),
    ((232, 239), (108, 108)),
    ((242, 242), (109, 109)),
    ((258, 262), (113, 113)),
    ((264, 270), (115, 115)),
    ((271, 278), (116, 116)),
    ((291, 295), (119, 119)),
    ((297, 304), (121, 121)),
    ((307, 307), (122, 122)),
    ((323, 327), (126, 126)),
    ((329, 335), (128, 128)),
    ((348, 352), (132, 132)),
    ((354, 361), (134, 134)),
    ((364, 364), (135, 135)),
)
