#!/usr/bin/node
/*
module.exports.esrever = function (list) {
	list.sort((a,b)=>b-a);
	return list;
}
*/
module.exports.esrever = function (list) {
  const reversedList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }

  return reversedList;
};

