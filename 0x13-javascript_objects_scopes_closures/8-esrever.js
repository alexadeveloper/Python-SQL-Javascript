#!/usr/bin/node
// class reversed version of a list
exports.esrever = function (list) {
  const rlist = [];
  let orden = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    rlist[orden] = list[i];
    orden--;
  }
  return rlist;
};
