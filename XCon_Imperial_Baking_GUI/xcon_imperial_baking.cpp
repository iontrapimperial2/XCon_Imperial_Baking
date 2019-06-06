#include "xcon_imperial_baking.h"
#include "ui_xcon_imperial_baking.h"

XCon_Imperial_Baking::XCon_Imperial_Baking(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::XCon_Imperial_Baking)
{
    ui->setupUi(this);
}

XCon_Imperial_Baking::~XCon_Imperial_Baking()
{
    delete ui;
}
