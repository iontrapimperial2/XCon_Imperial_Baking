#include "xcon_imperial_baking.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    XCon_Imperial_Baking w;
    w.show();

    return a.exec();
}
