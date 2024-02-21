//Author: Samyak Chakrabarty
//UID: 406-300-571
//UCLA EE 201A Lab 1

// *****************************************************************************
// *****************************************************************************
// Except as specified in the OpenAccess terms of use of Cadence or Silicon
// Integration Initiative, this material may not be copied, modified,
// re-published, uploaded, executed, or distributed in any way, in any medium,
// in whole or in part, without prior written permission from Cadence.
//
//                Copyright 2002-2005 Cadence Design Systems, Inc.
//                           All Rights Reserved.
//
// To distribute any derivative work based upon this file you must first contact
// Si2 @ contracts@si2.org.
//
// *****************************************************************************
// *****************************************************************************

#include <iostream>
#include <vector>
#include <numeric>
#include "oaDesignDB.h"
#include "bound_checker.h"

#include "/w/class.1/ee/ee201o/ee201ota/oa/examples/oa/common/commonTechObserver.h"
#include "/w/class.1/ee/ee201o/ee201ota/oa/examples/oa/common/commonLibDefListObserver.h"
#include "/w/class.1/ee/ee201o/ee201ota/oa/examples/oa/common/commonFunctions.h"

using namespace oa;
using namespace std;

static oaNativeNS ns;

int blk_violations = 0;

// ****************************************************************************
// printBBox()
//
// This function prints the given bounding box.
// ****************************************************************************
void
printBBox(oaBox &bbox)
{
    cout << "\t[{" << bbox.left() << "," << bbox.bottom()
        << "} , {" << bbox.right() << "," << bbox.top() << "}]" << endl
        << endl;
}

void
MyInstQuery::queryInst(oaInst *inst)
{
    oaString        instName;
    inst->getName(oaNs, instName);
    cout << "Violating instance: " << instName << endl;
    blk_violations++;
}

// ****************************************************************************
// opnBlockageQuery::queryShape()
//
// This function gets the blockages from the oaLayerRangeBlockageQuery. The 
// function prints the bounding box and type of the blockage.
// ****************************************************************************
void
opnBlockageQuery::queryBlockage(oaBlockage *blockage)
{
    oaBox       bbox;
    oaHierPath  hierPath;

    blockage->getBBox(bbox);

    cout << "Blockage Type: " << blockage->getType().getName() << endl;

    cout << "\tBounding Box: " << "[{" << bbox.left() << "," << bbox.bottom()
        << "} , {" << bbox.right() << "," << bbox.top() << "}]" << endl
        << endl;
}



// ****************************************************************************
// opnBlockageQuery::queryPlacementBlockage()
//
// This function gets the placementBlockages from the oaLayerRangeBlockageQuery.
// The queryBlockage function is reused to output the information.
// ****************************************************************************
void
opnBlockageQuery::queryPlacementBlockage(oaBlockage *blockage)
{
    queryBlockage(blockage);
}


// ****************************************************************************
// printDesignNames()
//
// This function gets the library, cell and view names associated with the open
// design and prints them.
// ****************************************************************************
void
printDesignNames(oaDesign *design)
{
    oaString    libName;
    oaString    cellName;
    oaString    viewName;

    // Library, cell and view names are obtained.
    design->getLibName(ns, libName);
    design->getCellName(ns, cellName);
    design->getViewName(ns, viewName);

    // Library, cell and view names are printed.
    cout << "\tThe library name for this design is : " << libName << endl;
    cout << "\tThe cell name for this design is : " << cellName << endl;
    cout << "\tThe view name for this design is : " << viewName << endl;
}

// ****************************************************************************
// void printNets()
//  
//  This function invokes the net iterator for the design and prints the names
//  of the nets one by one.
// ****************************************************************************
void
printNets(oaDesign *design)
{
    // Get the TopBlock of the current design
    oaBlock *block = design->getTopBlock();

    if (block) {
        oaString        netName;

        cout << "The following nets exist in this design." << endl;

        // Iterate over all nets in the design
        oaIter<oaNet>   netIterator(block->getNets());
        while (oaNet * net = netIterator.getNext()) {
            net->getName(ns, netName);
            cout << "\t" << netName << endl;
        }
    } else {
        cout << "There is no block in this design" << endl;
    }
}

// ****************************************************************************
// main()
//
// This is the top level function that opens the design, prints library, cell,
// and view names, creates nets, and iterates the design to print the net 
// names.
// ****************************************************************************
int
main(int    argc,
     char   *argv[])
{
    try {
        // Initialize OA with data model 3, since incremental technology
        // databases are supported by this application.
        oaDesignInit(oacAPIMajorRevNumber, oacAPIMinorRevNumber, 3);

        oaString                libPath("./DesignLib");
        oaString                library("DesignLib");
	    oaViewType      	*viewType = oaViewType::get(oacMaskLayout);
        oaString        	cell("s1494_bench");
       	oaString        	view("layout"); 
	    oaScalarName            libName(ns,
                                        library);
        oaScalarName            cellName(ns,
                                         cell);
        oaScalarName            viewName(ns,
                                         view);
	    oaScalarName    	libraryName(ns,library);
        // Setup an instance of the oaTech conflict observer.
        opnTechConflictObserver myTechConflictObserver(1);

        // Setup an instance of the oaLibDefList observer.
        opnLibDefListObserver   myLibDefListObserver(1);

        oaRegionQuery::init("oaRQSystem");

        // Read in the lib.defs file.
		oaLib *lib = oaLib::find(libraryName);

        if (!lib) {
            if (oaLib::exists(libPath)) {
                // Library does exist at this path but was not in lib.defs
                lib = oaLib::open(libraryName, libPath);
            } else {
            char *DMSystem=getenv("DMSystem");
            if(DMSystem){
                    lib = oaLib::create(libraryName, libPath, oacSharedLibMode, DMSystem);
                } else {
                    lib = oaLib::create(libraryName, libPath);
                }
            }
            if (lib) {
                // We need to update the user's lib.def file since we either
                // found or created the library without a lib.defs reference.
                updateLibDefsFile(libraryName, libPath);
            } else {
                // Print error mesage 
                cerr << "ERROR : Unable to create " << libPath << "/";
                cerr << library << endl;
                return(1);
            }
        }
		// Create the design with the specified viewType,
        // Opening it for a 'write' operation.
        cout << "The design is created and opened in 'write' mode." << endl;

        oaDesign    *design = oaDesign::open(libraryName, cellName, viewName,
                                             viewType, 'r');


		// Get the TopBlock for this design.
        oaBlock *block = design->getTopBlock();
	
		// If no TopBlock exist yet then create one.
        if (!block) {
            block = oaBlock::create(design);
        }


        // read from blockage_parsed.txt the 4 floats
        vector<float> blockage;
        ifstream blockageFile("blockage_parsed.txt");
        float blockageValue;
        while (blockageFile >> blockageValue) {
            blockage.push_back(blockageValue);
        }
        blockageFile.close();

        // if length of blockage is not 4, then error out and exit
        if (blockage.size() != 4) {
            cout << "ERROR: blockage_parsed.txt does not contain 4 floats" << endl;
            exit(1);
        }

        float x1 = blockage[0]*2000;
        float y1 = blockage[1]*2000;
        float x2 = blockage[2]*2000;
        float y2 = blockage[3]*2000;
        
        // we have this blockage. now query region to ensure nothing is there.
        oaBox box(x1, y1, x2, y2);

        cout << "The blockage checked is: (" << x1 << "," << y1 << ") - (" << x2 << "," << y2 << ")" << endl;

        MyInstQuery blkgquery;
        blkgquery.query(design, box);

        if (blk_violations == 0) {
            cout << "No blockage violations found!" << endl;
        } else {
            cout << "Blockage violations found: " << blk_violations << endl;
        }

        // The design is closed.   
        design->close();

        // The library is closed.   
        lib->close();

    } catch (oaCompatibilityError &ex) {
        handleFBCError(ex);
        exit(1);

    } catch (oaException &excp) {
        cout << "ERROR: " << excp.getMsg() << endl;
        exit(1);
    }

    return 0;
}