#ifndef TCPSERVER_H
#define TCPSERVER_H

#include "strategylab.h"
#include "functional.h"

#include <QTcpServer>
#include <QTcpSocket>
#include <QJsonDocument>
#include <QJsonObject>

/**
*   @brief Реализация сервера для проверки лабораторных работ по паттерну стратегии
*/
class TcpServer : public QObject
{
    Q_OBJECT

private:
    QTcpServer* mTcpServer;
    QTcpSocket* mTcpSocket;
    StrategyLab* lab;
    Functional* githubManager;
    QJsonDocument docJson;
    QJsonParseError docJsonError;

public:
    explicit TcpServer(QObject *parent = nullptr);
    void sendToClient(bool answer);

private:
    bool parsingJson(QJsonDocument, QString*, int*, QList<QString>*);

public slots:
    void slotNewConnection();
    void slotClientDisconnected();
    void slotReadingDataJson();
};

#endif // TCPSERVER_H
