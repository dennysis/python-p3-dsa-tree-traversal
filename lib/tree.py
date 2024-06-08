class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, id, node=None):
        if node is None:
            node = self.root

        if node['id'] == id:
            return node
        
        for child in node['children']:
            result = self.get_element_by_id(id, child)
            if result:
                return result
        
        return None
