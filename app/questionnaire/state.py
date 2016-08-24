'''
  Everything in this class and the following packages is potentially serialized to the database and
  therefore can cause issues if the code changes between deployments and sessions remain in the database.


  schema - the entire schema (once it's parsed) this is needed as repeated elements modifies the schema, so the modified
  version needs to be recovered

  questionnaire_state - the doubly linked listed, i.e. the Node object, its associated Block State and all the child
  states

'''


class State(object):
    def __init__(self, schema, current_node, first_node, archive, submitted_at, valid_locations):
        self.schema = schema
        self.current = current_node
        self.first = first_node
        self.archive = archive
        self.submitted_at = submitted_at
        self.valid_locations = valid_locations
