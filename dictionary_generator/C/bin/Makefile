SHEDSKIN_LIBDIR=/usr/share/shedskin/lib
CC=g++
CCFLAGS=-O2 -march=native -Wno-deprecated $(CPPFLAGS) -I. -I${SHEDSKIN_LIBDIR}
LFLAGS=-lgc -lpcre $(LDFLAGS)

CPPFILES=/media/sf_Ubuntu-Server/pdfcrack/word_permutation/bin/word_permutation.cpp \
	${SHEDSKIN_LIBDIR}/re.cpp \
	${SHEDSKIN_LIBDIR}/itertools.cpp \
	${SHEDSKIN_LIBDIR}/builtin.cpp

HPPFILES=/media/sf_Ubuntu-Server/pdfcrack/word_permutation/bin/word_permutation.hpp \
	${SHEDSKIN_LIBDIR}/re.hpp \
	${SHEDSKIN_LIBDIR}/itertools.hpp \
	${SHEDSKIN_LIBDIR}/builtin.hpp

all:	word_permutation

word_permutation:	$(CPPFILES) $(HPPFILES)
	$(CC)  $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o word_permutation

word_permutation_prof:	$(CPPFILES) $(HPPFILES)
	$(CC) -pg -ggdb $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o word_permutation_prof

word_permutation_debug:	$(CPPFILES) $(HPPFILES)
	$(CC) -g -ggdb $(CCFLAGS) $(CPPFILES) $(LFLAGS) -o word_permutation_debug

clean:
	rm -f word_permutation word_permutation_prof word_permutation_debug

.PHONY: all clean

