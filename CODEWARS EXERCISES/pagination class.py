class PaginationHelper:

      # The constructor takes in an array of items and a integer indicating
      # how many items fit within a single page
      def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page



      # returns the number of items within the entire collection
      def item_count(self):
        return len(self.collection)

      # returns the number of pages
      def page_count(self):
        if len(self.collection) % self.items_per_page != 0:
            return (len(self.collection) // self.items_per_page) + 1

        else:
            return (len(self.collection) // self.items_per_page)

      # returns the number of items on the current page. page_index is zero based
      # this method should return -1 for page_index values that are out of range
      def page_item_count(self,page_index):
        if (page_index < 0 or page_index > self.page_count()-1 or page_index == None):
            return -1
        return len(self.collection[(self.items_per_page * page_index):(self.items_per_page * (page_index + 1))])


      # determines what page an item is on. Zero based indexes.
      # this method should return -1 for item_index values that are out of range
      def page_index(self,item_index):
        if (item_index < 0 or item_index > (len(self.collection) -1)):
            return -1

        return item_index // self.items_per_page

book = PaginationHelper([1,2,3,4,5,6], 3)
print(book.item_count())
print(book.page_count())
print(book.page_item_count(0))