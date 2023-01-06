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
                    "presenta"):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
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
  
  bc_rule.bc_rule('has_symptom_tumor', This_rule_base, 'has_symptom',
                  has_symptom_tumor, None,
                  (contexts.variable('tumor'),
                   contexts.variable('symptom'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('tumor'),
                   contexts.variable('symptom'),
                   contexts.variable('relationship'),))
  
  bc_rule.bc_rule('has_related_name_category', This_rule_base, 'has_category',
                  has_related_name_category, None,
                  (contexts.variable('name'),
                   contexts.variable('category'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('name'),
                   contexts.variable('category'),
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


Krb_filename = '../examples/system/bc_system.krb'
Krb_lineno_map = (
    ((14, 18), (3, 3)),
    ((20, 27), (5, 5)),
    ((40, 44), (22, 22)),
    ((46, 52), (24, 24)),
    ((55, 55), (25, 25)),
    ((71, 75), (29, 29)),
    ((77, 83), (31, 31)),
    ((86, 86), (32, 32)),
    ((102, 106), (35, 35)),
    ((108, 114), (37, 37)),
    ((117, 117), (38, 38)),
)
