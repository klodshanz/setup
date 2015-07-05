// #########################################################
// String ReplaceAll with Regular Expression
// #########################################################

def text = "01-07-2015 (22:33)"

def new_text = text.replaceAll( /(\d+)-(\d+)-(\d+)/) {
	// remember "all". Other parameters are groups in the RegEx
	all, dd, mm, yyyy -> "${yyyy}-${mm}-${dd}"
}

assert new_text == "2015-07-01 (22:33)"
