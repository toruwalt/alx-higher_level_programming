#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (x of list) {
    if (x === searchElement) {
	    count++;
    }
  }
  return count;
}
