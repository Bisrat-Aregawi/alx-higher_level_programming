#!/usr/bin/node
exports.callMeMoby = function (x, fun) {
  if (x >= 0) {
    while (x--) {
      fun();
    }
  }
};
