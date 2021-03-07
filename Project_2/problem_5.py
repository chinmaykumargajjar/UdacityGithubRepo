import hashlib

def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()


class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Block("timestamp", "data", 0)
            return

        # Move to the tail (the last node)
        node = self.head
        prev = self.head

        while node.next:
            prev = node
            node = node.next

        node.next = Block("timestamp", "data", node.hash)
        return



