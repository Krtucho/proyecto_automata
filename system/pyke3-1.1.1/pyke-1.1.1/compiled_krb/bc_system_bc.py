# bc_system_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

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
                    "da"):
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
  
  bc_rule.bc_rule('has_symptom_tumor', This_rule_base, 'has_symptom',
                  has_symptom_tumor, None,
                  (contexts.variable('tumor'),
                   contexts.variable('symptom'),
                   contexts.variable('relationship'),),
                  (),
                  (contexts.variable('tumor'),
                   contexts.variable('symptom'),
                   contexts.variable('relationship'),))


Krb_filename = '../examples/system/bc_system.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 26), (4, 4)),
    ((29, 29), (5, 5)),
)
