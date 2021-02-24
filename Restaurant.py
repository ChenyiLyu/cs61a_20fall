
def search(query, ranking = lambda r: -r.stars):
	results = [r for r in Restaurant.all if query in r.name]

	return sorted(results, key = ranking)


Restaurant('Thai Delight', 2)
Restaurant('Thai Basil', 3)
Restaurant('Top Dog', 5)

# Return restaurants by search key word.
results = search('Thai')
# for each restaurant in returned results, return the 3 most similar ones to SELF.
for r in results:
	print(r, 'is similar to', r.similar(3))

class Restaurant:
	all = []

	def __init__(self, name, star):
		self.name = name
		self.star = star
		Restaurant.all.append[self]

	def similar(self, k): 
		"Return the K most similar restaurants to SELF, using SIMILARITY for comparison."

		others = list(Restaurants.all)
		others.remove(self)
		return sorted(others, key = lambda r: -r.similarity(r, self))

	def __repr__(self):
		return '<' + self.name + '>'


def similar(self, r, similarity):
	"Return the K most similar restaurants to SELF, using SIMILARITY for comparison"
	r = list(Restaurants.all) # return all restaurants

	others.
	return sorted(others, key = )