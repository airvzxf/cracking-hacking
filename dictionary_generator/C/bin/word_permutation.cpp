#include "builtin.hpp"
#include "itertools.hpp"
#include "word_permutation.hpp"

namespace __word_permutation__ {

str *const_0, *const_1, *const_10, *const_11, *const_12, *const_13, *const_14, *const_15, *const_16, *const_17, *const_18, *const_19, *const_2, *const_20, *const_21, *const_22, *const_23, *const_24, *const_25, *const_26, *const_27, *const_28, *const_29, *const_3, *const_30, *const_31, *const_32, *const_33, *const_34, *const_35, *const_4, *const_5, *const_6, *const_7, *const_8, *const_9;

using __itertools__::combinations;

list<str *> *wordList;
tuple2<str *, str *> *c;
file *f;
str *__name__;
__iter<tuple2<str *, str *> *> *__2, *__3;
__ss_int __0, __1, __4, w;
__iter<tuple2<str *, str *> *>::for_in_loop __5;


class list_comp_0 : public __iter<str *> {
public:
    tuple2<str *, str *> *__6;
    str *x;
    __ss_int __8;
    tuple2<str *, str *>::for_in_loop __9;
    __iter<str *> *__7;

    int __last_yield;

    list_comp_0();
    str * __get_next();
};


list_comp_0::list_comp_0() {
    __last_yield = -1;
}

str * list_comp_0::__get_next() {
    if(!__last_yield) goto __after_yield_0;
    __last_yield = 0;

    FOR_IN(x,c,6,8,9)
        __result = __str(x);
        return __result;
        __after_yield_0:;
    END_FOR

    __stop_iteration = true;
}

void __init() {
    const_0 = new str("__main__");
    const_1 = new str("Airv");
    const_2 = new str("airv");
    const_3 = new str("Zxf");
    const_4 = new str("zxf");
    const_5 = new str("Rovi");
    const_6 = new str("rovi");
    const_7 = new str("Lvvg");
    const_8 = new str("lvvg");
    const_9 = new str("30");
    const_10 = new str("08");
    const_11 = new str("83");
    const_12 = new str("1983");
    const_13 = new str("830830");
    const_14 = new str("300883");
    const_15 = new str("19830830");
    const_16 = new str("30081983");
    const_17 = new str("19831983");
    const_18 = new str("2468");
    const_19 = new str("02468");
    const_20 = new str("24680");
    const_21 = new str("Banorte");
    const_22 = new str("banorte");
    const_23 = new str("Bqh");
    const_24 = new str("Nabiki");
    const_25 = new str("nabiki");
    const_26 = __char_cache[32];;
    const_27 = __char_cache[33];;
    const_28 = __char_cache[45];;
    const_29 = new str("permutation-list.txt");
    const_30 = __char_cache[119];;
    const_31 = new str("Working...");
    const_32 = new str("");
    const_33 = __char_cache[10];;
    const_34 = new str("All permutations have been created.");
    const_35 = new str("Finished!");

    __name__ = new str("__main__");

    if (__eq(__name__, const_0)) {
        wordList = (new list<str *>(29,const_1,const_2,const_3,const_4,const_5,const_6,const_7,const_8,const_9,const_10,const_11,const_12,const_13,const_14,const_15,const_16,const_17,const_18,const_19,const_20,const_21,const_22,const_23,const_24,const_25,const_26,const_27,const_28,const_28));
        f = open(const_29, const_30);
        print2(NULL,0,1, const_31);

        FAST_FOR(w,0,(len(wordList)+1),1,0,1)

            FOR_IN(c,combinations(wordList, w),2,4,5)
                f->write((const_32)->join(new list_comp_0()));
                f->write(const_33);
            END_FOR

        END_FOR

        print2(NULL,0,1, const_34);
        f->close();
        print2(NULL,0,1, const_35);
    }
}

} // module namespace

int main(int, char **) {
    __shedskin__::__init();
    __itertools__::__init();
    __shedskin__::__start(__word_permutation__::__init);
}
