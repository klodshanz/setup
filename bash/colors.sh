echo
printf "                40m     41m     42m     43m     44m     45m     46m     47m"
#for back in 0 1 2 3 4 5 6 7; do printf "  4${back}m   "; done
echo
for front in "" 30 31 32 33 34 35 36 37; do
	for weight in "  " "1;"; do
		if  (! ( [ "$front" == "" ] && [ "$weight" == "  " ] )); then
			printf "%5sm" "${weight}${front}"
			printf " \033[%sm%s\033[0m  " "$weight$front" " Text"
			for back in 0 1 2 3 4 5 6 7; do
				printf " \033[4%s;%sm%s\033[0m  " $back $weight$front " gYw "
			done
			echo
		fi
	done
done
echo

