
class State(object):
    def __init__(self, schema, current_node, first_node, archive, submitted_at, valid_locations):
        self.schema = schema
        self.current = current_node
        self.first = first_node
        self.archive = archive
        self.submitted_at = submitted_at
        self.valid_locations = valid_locations
