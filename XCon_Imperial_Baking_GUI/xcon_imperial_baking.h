#ifndef XCON_IMPERIAL_BAKING_H
#define XCON_IMPERIAL_BAKING_H

#include <QMainWindow>

namespace Ui {
class XCon_Imperial_Baking;
}

class XCon_Imperial_Baking : public QMainWindow
{
    Q_OBJECT

public:
    explicit XCon_Imperial_Baking(QWidget *parent = 0);
    ~XCon_Imperial_Baking();

private:
    Ui::XCon_Imperial_Baking *ui;
};

#endif // XCON_IMPERIAL_BAKING_H
