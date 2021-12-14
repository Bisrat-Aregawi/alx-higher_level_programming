#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let count = 0;
  list.forEach(elem => {
    if (elem === searchElement) count++;
  });
  return count;
};
