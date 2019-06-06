/********************************************************************************
** Form generated from reading UI file 'xcon_imperial_baking.ui'
**
** Created by: Qt User Interface Compiler version 5.7.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_XCON_IMPERIAL_BAKING_H
#define UI_XCON_IMPERIAL_BAKING_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_XCon_Imperial_Baking
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout;
    QSpacerItem *horizontalSpacer_3;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer_4;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer_5;
    QGroupBox *groupBox_3;
    QSpacerItem *horizontalSpacer;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout_3;
    QGridLayout *gridLayout_3;
    QRadioButton *radioButton_ch4;
    QRadioButton *radioButton_ch6;
    QRadioButton *radioButton_ch2;
    QRadioButton *radioButton_ch5;
    QRadioButton *radioButton_ch1;
    QRadioButton *radioButton_ch3;
    QRadioButton *radioButton_ch7;
    QRadioButton *radioButton_ch8;
    QSpacerItem *verticalSpacer;
    QSpacerItem *verticalSpacer_7;
    QSpacerItem *horizontalSpacer_4;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_2;
    QGridLayout *gridLayout_2;
    QRadioButton *radioButton_monitoring;
    QPushButton *pushButton_import;
    QLineEdit *lineEdit_data;
    QPushButton *pushButton_browse;
    QFrame *line;
    QVBoxLayout *verticalLayout_temp;
    QVBoxLayout *verticalLayout_pressure;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *XCon_Imperial_Baking)
    {
        if (XCon_Imperial_Baking->objectName().isEmpty())
            XCon_Imperial_Baking->setObjectName(QStringLiteral("XCon_Imperial_Baking"));
        XCon_Imperial_Baking->resize(1272, 735);
        centralWidget = new QWidget(XCon_Imperial_Baking);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 0, 2, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_3, 5, 0, 1, 1);

        verticalSpacer_4 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_4, 2, 0, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 1, 1, 1);

        verticalSpacer_5 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_5, 4, 0, 1, 1);

        groupBox_3 = new QGroupBox(centralWidget);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));

        gridLayout->addWidget(groupBox_3, 4, 4, 2, 1);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 4, 1, 1);

        groupBox_2 = new QGroupBox(centralWidget);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        verticalLayout_3 = new QVBoxLayout(groupBox_2);
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setContentsMargins(11, 11, 11, 11);
        verticalLayout_3->setObjectName(QStringLiteral("verticalLayout_3"));
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setSpacing(6);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        radioButton_ch4 = new QRadioButton(groupBox_2);
        radioButton_ch4->setObjectName(QStringLiteral("radioButton_ch4"));

        gridLayout_3->addWidget(radioButton_ch4, 1, 1, 1, 1);

        radioButton_ch6 = new QRadioButton(groupBox_2);
        radioButton_ch6->setObjectName(QStringLiteral("radioButton_ch6"));

        gridLayout_3->addWidget(radioButton_ch6, 2, 1, 1, 1);

        radioButton_ch2 = new QRadioButton(groupBox_2);
        radioButton_ch2->setObjectName(QStringLiteral("radioButton_ch2"));

        gridLayout_3->addWidget(radioButton_ch2, 0, 1, 1, 1);

        radioButton_ch5 = new QRadioButton(groupBox_2);
        radioButton_ch5->setObjectName(QStringLiteral("radioButton_ch5"));

        gridLayout_3->addWidget(radioButton_ch5, 2, 0, 1, 1);

        radioButton_ch1 = new QRadioButton(groupBox_2);
        radioButton_ch1->setObjectName(QStringLiteral("radioButton_ch1"));

        gridLayout_3->addWidget(radioButton_ch1, 0, 0, 1, 1);

        radioButton_ch3 = new QRadioButton(groupBox_2);
        radioButton_ch3->setObjectName(QStringLiteral("radioButton_ch3"));

        gridLayout_3->addWidget(radioButton_ch3, 1, 0, 1, 1);

        radioButton_ch7 = new QRadioButton(groupBox_2);
        radioButton_ch7->setObjectName(QStringLiteral("radioButton_ch7"));

        gridLayout_3->addWidget(radioButton_ch7, 3, 0, 1, 1);

        radioButton_ch8 = new QRadioButton(groupBox_2);
        radioButton_ch8->setObjectName(QStringLiteral("radioButton_ch8"));

        gridLayout_3->addWidget(radioButton_ch8, 3, 1, 1, 1);


        verticalLayout_3->addLayout(gridLayout_3);


        gridLayout->addWidget(groupBox_2, 2, 4, 2, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 3, 0, 1, 1);

        verticalSpacer_7 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer_7, 1, 0, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_4, 0, 3, 1, 1);

        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        verticalLayout_2 = new QVBoxLayout(groupBox);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        gridLayout_2 = new QGridLayout();
        gridLayout_2->setSpacing(6);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        radioButton_monitoring = new QRadioButton(groupBox);
        radioButton_monitoring->setObjectName(QStringLiteral("radioButton_monitoring"));

        gridLayout_2->addWidget(radioButton_monitoring, 0, 2, 1, 1);

        pushButton_import = new QPushButton(groupBox);
        pushButton_import->setObjectName(QStringLiteral("pushButton_import"));

        gridLayout_2->addWidget(pushButton_import, 0, 4, 1, 1);

        lineEdit_data = new QLineEdit(groupBox);
        lineEdit_data->setObjectName(QStringLiteral("lineEdit_data"));

        gridLayout_2->addWidget(lineEdit_data, 0, 1, 1, 1);

        pushButton_browse = new QPushButton(groupBox);
        pushButton_browse->setObjectName(QStringLiteral("pushButton_browse"));

        gridLayout_2->addWidget(pushButton_browse, 0, 0, 1, 1);

        line = new QFrame(groupBox);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout_2->addWidget(line, 0, 3, 1, 1);


        verticalLayout_2->addLayout(gridLayout_2);


        gridLayout->addWidget(groupBox, 1, 1, 1, 4);

        verticalLayout_temp = new QVBoxLayout();
        verticalLayout_temp->setSpacing(6);
        verticalLayout_temp->setObjectName(QStringLiteral("verticalLayout_temp"));

        gridLayout->addLayout(verticalLayout_temp, 2, 1, 2, 3);

        verticalLayout_pressure = new QVBoxLayout();
        verticalLayout_pressure->setSpacing(6);
        verticalLayout_pressure->setObjectName(QStringLiteral("verticalLayout_pressure"));

        gridLayout->addLayout(verticalLayout_pressure, 4, 1, 2, 3);


        verticalLayout->addLayout(gridLayout);

        XCon_Imperial_Baking->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(XCon_Imperial_Baking);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1272, 26));
        XCon_Imperial_Baking->setMenuBar(menuBar);
        mainToolBar = new QToolBar(XCon_Imperial_Baking);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        XCon_Imperial_Baking->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(XCon_Imperial_Baking);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        XCon_Imperial_Baking->setStatusBar(statusBar);

        retranslateUi(XCon_Imperial_Baking);

        QMetaObject::connectSlotsByName(XCon_Imperial_Baking);
    } // setupUi

    void retranslateUi(QMainWindow *XCon_Imperial_Baking)
    {
        XCon_Imperial_Baking->setWindowTitle(QApplication::translate("XCon_Imperial_Baking", "XCon_Imperial_Baking", 0));
        groupBox_3->setTitle(QApplication::translate("XCon_Imperial_Baking", "GroupBox", 0));
        groupBox_2->setTitle(QApplication::translate("XCon_Imperial_Baking", "GroupBox", 0));
        radioButton_ch4->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch6->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch2->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch5->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch1->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch3->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch7->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        radioButton_ch8->setText(QApplication::translate("XCon_Imperial_Baking", "RadioButton", 0));
        groupBox->setTitle(QApplication::translate("XCon_Imperial_Baking", "GroupBox", 0));
        radioButton_monitoring->setText(QApplication::translate("XCon_Imperial_Baking", "Monitoring", 0));
        pushButton_import->setText(QApplication::translate("XCon_Imperial_Baking", "go", 0));
        pushButton_browse->setText(QApplication::translate("XCon_Imperial_Baking", "Browse", 0));
    } // retranslateUi

};

namespace Ui {
    class XCon_Imperial_Baking: public Ui_XCon_Imperial_Baking {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_XCON_IMPERIAL_BAKING_H
