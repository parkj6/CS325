default: ch pair

checker:
	python checker.py

ch:
	chmod 755 *.py

run:
	python3 Imp2.py
pair:
	./pairgen pair10.in 10
	./pairgen pair100.in 100
	./pairgen pair500.in 500
	./pairgen pair1000.in 1000
	./pairgen pair2000.in 2000
	./pairgen pair4000.in 4000
	./pairgen pair5000.in 5000

clean:
	rm -rf ./*~
	rm -rf ./__pycache__
	rm -f *.in
	rm -f *.out
	rm -f imp2out_* 
	rm -f testpair* 

