#!/usr/bin/node
exports.esrever = function (list) {
  let i = 0;
  return list.map(() => {
    i++;
    return list[list.length - i];
  });
};
