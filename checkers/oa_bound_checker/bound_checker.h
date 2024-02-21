
#include <iostream>
#include "oaDesignDB.h"


using namespace oa;
using namespace std;


class MyInstQuery : public oaInstQuery {
public:
    MyInstQuery()
        : oaInstQuery()
    {
    }
    ~MyInstQuery()
    {
    }
    void queryInst(oaInst *inst);
    oaNativeNS              oaNs;
};

class opnBlockageQuery : public oaBlockageQuery {
public:
    opnBlockageQuery()
    : oaBlockageQuery()
    {
    }
    ~opnBlockageQuery()
    {
    }
    void                    queryBlockage(oaBlockage *shape);
    virtual void            queryPlacementBlockage(oaBlockage *blockage);
    oaNativeNS              oaNs;
};
