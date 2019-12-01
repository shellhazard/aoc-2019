let lineReader = require('readline').createInterface({
 	input: require('fs').createReadStream('input.txt')
});

sum = 0
lineReader.on('line', function(line) {
 	let result = calcfuel(line)
 	sum += result
 	while (result > 0) {
 		result = calcfuel(result)
 		sum += result
 	}
 	console.log(sum)
});

calcfuel = function(input) {
	let result = Math.floor(parseInt(input) / 3) - 2
	if (result < 0) result = 0
	return result
}