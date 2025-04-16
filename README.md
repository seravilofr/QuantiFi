# 📈 Quantifi- A global economic index dashboard

A Python-powered web tool to visualize major economic indices from around the world.  
This project focuses on providing an up-to-date view of the most relevant stock market indices for key global economies and regions.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-WIP-orange)

---

## 🌍 Included Economic Indices

| Country/Region        | Index Name                      | Ticker        | Description                                                              |
|------------------------|----------------------------------|---------------|--------------------------------------------------------------------------|
| 🇺🇸 United States       | S&P 500                          | ^GSPC         | 500 largest companies listed in the U.S.                                 |
| 🇺🇸 United States       | Dow Jones Industrial Average     | ^DJI          | 30 major U.S. industrial companies                                       |
| 🇺🇸 United States       | Nasdaq Composite                 | ^IXIC         | Tech-heavy index including 3,000+ stocks                                 |
| 🇺🇸 United States       | Nasdaq-100                       | ^NDX          | Top 100 non-financial companies listed on the Nasdaq                     |
| 🇪🇺 European Union      | Euro Stoxx 50                    | ^STOXX50E     | 50 major companies in the eurozone                                       |
| 🇪🇺 European Union      | MSCI EMU                         | EZU           | Stocks from countries in the eurozone                                    |
| 🇪🇺 European Union      | STOXX Europe 600                | SXXP          | 600 companies across Europe (EU and non-EU)                              |
| 🇫🇷 France              | CAC 40                           | ^FCHI         | 40 largest listed French companies                                       |
| 🇩🇪 Germany             | DAX 40                           | ^GDAXI        | 40 major listed German companies                                         |
| 🇬🇧 United Kingdom      | FTSE 100                         | ^FTSE         | 100 largest companies listed in London                                  |
| 🇮🇹 Italy               | FTSE MIB                         | FTSEMIB.MI    | 40 major Italian companies                                               |
| 🇨🇦 Canada              | S&P/TSX Composite                | ^GSPTSE       | Main Canadian stock market index                                         |
| 🇨🇳 China               | SSE Composite                    | 000001.SS     | Broad index of all stocks on the Shanghai Stock Exchange                 |
| 🇨🇳 China               | CSI 300                          | 000300.SS     | 300 largest market cap companies in China                                |
| 🇰🇷 South Korea         | KOSPI                            | ^KS11         | Korea Composite Stock Price Index                                        |
| 🇯🇵 Japan               | Nikkei 225                       | ^N225         | 225 top Japanese companies                                               |
| 🇳🇱 Netherlands         | AEX                              | ^AEX          | 25 major Dutch companies                                                 |
| 🇪🇸 Spain              | IBEX 35                          | ^IBEX         | 35 largest listed Spanish companies                                      |
| 🌍 Global              | MSCI World                       | URTH          | Global developed market stocks                                           |
| 🌍 Global              | MSCI ACWI                        | ACWI          | All Country World Index: developed + emerging markets                    |
| 🌍 Global              | FTSE All-World                   | FTWD          | Broad index of global developed and emerging market equities             |
| 🇪🇺 EU-wide (Euronext)  | Euronext 100                     | N100          | 100 largest companies listed on Euronext exchanges                       |

---

## ⚙️ Installation

```bash
git clone https://github.com/seravilofr/QuantiFi.git
cd quantifi
pip install -r requirements.txt
