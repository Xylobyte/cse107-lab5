COURSE = cse107
GROUP_NAME = donovan_griego
ASSIGNMENT = lab5
TARGETS = cipher.py fractions.py luhns.py README.md
zip: $(TARGETS)
	zip $(COURSE)_$(GROUP_NAME)_$(ASSIGNMENT).zip $(TARGETS)