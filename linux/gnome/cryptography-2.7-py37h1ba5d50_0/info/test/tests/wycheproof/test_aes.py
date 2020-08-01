         \
	(((x) & BIT_MASK_QUEUEMACID_HIQ_V1_8822B)                              \
	 << BIT_SHIFT_QUEUEMACID_HIQ_V1_8822B)
#define BIT_GET_QUEUEMACID_HIQ_V1_8822B(x)                                     \
	(((x) >> BIT_SHIFT_QUEUEMACID_HIQ_V1_8822B) &                          \
	 BIT_MASK_QUEUEMACID_HIQ_V1_8822B)

#define BIT_SHIFT_QUEUEAC_HIQ_V1_8822B 23
#define BIT_MASK_QUEUEAC_HIQ_V1_8822B 0x3
#define BIT_QUEUEAC_HIQ_V1_8822B(x)                                            \
	(((x) & BIT_MASK_QUEUEAC_HIQ_V1_8822B)                                 \
	 << BIT_SHIFT_QUEUEAC_HIQ_V1_8822B)
#define BIT_GET_QUEUEAC_HIQ_V1_8822B(x)                                        \
	(((x) >> BIT_SHIFT_QUEUEAC_HIQ_V1_8822B) &                             \
	 BIT_MASK_QUEUEAC_HIQ_V1_8822B)

#define BIT_TIDEMPTY_HIQ_V1_8822B BIT(22)

#define BIT_SHIFT_TAIL_PKT_HIQ_V2_8822B 11
#define BIT_MASK_TAIL_PKT_HIQ_V2_8822B 0x7ff
#define BIT_TAIL_PKT_HIQ_V2_8822B(x)                                           \
	(((x) & BIT_MASK_TAIL_PKT_HIQ_V2_8822B)                                \
	 << BIT_SHIFT_TAIL_PKT_HIQ_V2_8822B)
#define BIT_GET_TAIL_PKT_HIQ_V2_8822B(x)                                       \
	(((x) >> BIT_SHIFT_TAIL_PKT_HIQ_V2_8822B) &                            \
	 BIT_MASK_TAIL_PKT_HIQ_V2_8822B)

#define BIT_SHIFT_HEAD_PKT_HIQ_V1_8822B 0
#define BIT_MASK_HEAD_PKT_HIQ_V1_8822B 0x7ff
#define BIT_HEAD_PKT_HIQ_V1_8822B(x)                                           \
	(((x) & BIT_MASK_HEAD_PKT_HIQ_V1_8822B)                                \
	 << BIT_SHIFT_HEAD_PKT_HIQ_V1_8822B)
#define BIT_GET_HEAD_PKT_HIQ_V1_8822B(x)                                       \
	(((x) >> BIT_SHIFT_HEAD_PKT_HIQ_V1_8822B) &                            \
	 BIT_MASK_HEAD_PKT_HIQ_V1_8822B)

/* 2 REG_BCNQ_INFO_8822B */

#define BIT_SHIFT_BCNQ_HEAD_PG_V1_8822B 0
#define BIT_MASK_BCNQ_HEAD_PG_V1_8822B 0xfff
#define BIT_BCNQ_HEAD_PG_V1_8822B(x)                                           \
	(((x) & BIT_MASK_BCNQ_HEAD_PG_V1_8822B)                                \
	 << BIT_SHIFT_BCNQ_HEAD_PG_V1_8822B)
#define BIT_GET_BCNQ_HEAD_PG_V1_8822B(x)                                       \
	(((x) >> BIT_SHIFT_BCNQ_HEAD_PG_V1_8822B) &                            \
	 BIT_MASK_BCNQ_HEAD_PG_V1_8822B)

/* 2 REG_TXPKT_EMPTY_8822B */
#define BIT_BCNQ_EMPTY_8822B BIT(11)
#define BIT_HQQ_EMPTY_8822B BIT(10)
#define BIT_MQQ_EMPTY_8822B BIT(9)
#define BIT_MGQ_CPU_EMPTY_8822B BIT(8)
#define BIT_AC7Q_EMPTY_8822B BIT(7)
#define BIT_AC6Q_EMPTY_8822B BIT(6)
#define BIT_AC5Q_EMPTY_8822B BIT(5)
#define BIT_AC4Q_EMPTY_8822B BIT(4)
#define BIT_AC3Q_EMPTY_8822B BIT(3)
#define BIT_AC2Q_EMPTY_8822B BIT(2)
#define BIT_AC1Q_EMPTY_8822B BIT(1)
#define BIT_AC0Q_EMPTY_8822B BIT(0)

/* 2 REG_CPU_MGQ_INFO_8822B */
#define BIT_BCN1_POLL_8822B BIT(30)
#define BIT_CPUMGT_POLL_8822B BIT(29)
#define BIT_BCN_POLL_8822B BIT(28)
#define BIT_CPUMGQ_FW_NUM_V1_8822B BIT(12)

#define BIT_SHIFT_FW_FREE_TAIL_V1_8822B 0
#define BIT_MASK_FW_FREE_TAIL_V1_8822B 0xfff
#define BIT_FW_FREE_TAIL_V1_8822B(x)                                           \
	(((x) & BIT_MASK_FW_FREE_TAIL_V1_8822B)                                \
	 << BIT_SHIFT_FW_FREE_TAIL_V1_8822B)
#define BIT_GET_FW_FREE_TAIL_V1_8822B(x)                                       \
	(((x) >> BIT_SHIFT_FW_FREE_TAIL_V1_8822B) &                            \
	 BIT_MASK_FW_FREE_TAIL_V1_8822B)

/* 2 REG_FWHW_TXQ_CTRL_8822B */
#define BIT_RTS_LIMIT_IN_OFDM_8822B BIT(23)
#define BIT_EN_BCNQ_DL_8822B BIT(22)
#define BIT_EN_RD_RESP_NAV_BK_8822B BIT(21)
#define BIT_EN_WR_FREE_TAIL_8822B BIT(20)

#define BIT_SHIFT_EN_QUEUE_RPT_8822B 8
#define BIT_MASK_EN_QUEUE_RPT_8822B 0xff
#define BIT_EN_QUEUE_RPT_8822B(x)                                              \
	(((x) & BIT_MASK_EN_QUEUE_RPT_8822B) << BIT_SHIFT_EN_QUEUE_RPT_8822B)
#define BIT_GET_EN_QUEUE_RPT_8822B(x)                                          \
	(((x) >> BIT_SHIFT_EN_QUEUE_RPT_8822B) & BIT_MASK_EN_QUEUE_RPT_8822B)

#define BIT_EN_RTY_BK_8822B BIT(7)
#define BIT_EN_USE_INI_RAT_8822B BIT(6)
#define BIT_EN_RTS_NAV_BK_8822B BIT(5)
#define BIT_DIS_SSN_CHECK_8822B BIT(4)
#define BIT_MACID_MATCH_RTS_8822B BIT(3)
#define BIT_EN_BCN_TRXRPT_V1_8822B BIT(2)
#define BIT_EN_FTMACKRPT_8822B BIT(1)
#define BIT_EN_FTMRPT_8822B BIT(0)

/* 2 REG_DATAFB_SEL_8822B */
#define BIT__R_EN_RTY_BK_COD_8822B BIT(2)

#define BIT_SHIFT__R_DATA_FALLBACK_SEL_8822B 0
#define BIT_MASK__R_DATA_FALLBACK_SEL_8822B 0x3
#define BIT__R_DATA_FALLBACK_SEL_8822B(x)                                      \
	(((x) & BIT_MASK__R_DATA_FALLBACK_SEL_8822B)                           \
	 << BIT_SHIFT__R_DATA_FALLBACK_SEL_8822B)
#define BIT_GET__R_DATA_FALLBACK_SEL_8822B(x)                                  \
	(((x) >> BIT_SHIFT__R_DATA_FALLBACK_SEL_8822B) &                       \
	 BIT_MASK__R_DATA_FALLBACK_SEL_8822B)

/* 2 REG_BCNQ_BDNY_V1_8822B */

#define BIT_SHIFT_BCNQ_PGBNDY_V1_8822B 0
#define BIT_MASK_BCNQ_PGBNDY_V1_8822B 0xfff
#define BIT_BCNQ_PGBNDY_V1_8822B(x)                                            \
	(((x) & BIT_MASK_BCNQ_PGBNDY_V1_8822B)                                 \
	 << BIT_SHIFT_BCNQ_PGBNDY_V1_8822B)
#define BIT_GET_BCNQ_PGBNDY_V1_8822B(x)                                        \
	(((x) >> BIT_SHIFT_BCNQ_PGBNDY_V1_8822B) &                             \
	 BIT_MASK_BCNQ_PGBNDY_V1_8822B)

/* 2 REG_LIFETIME_EN_8822B */
#define BIT_BT_INT_CPU_8822B BIT(7)
#define BIT_BT_INT_PTA_8822B BIT(6)
#define BIT_EN_CTRL_RTYBIT_8822B BIT(4)
#define BIT_LIFETIME_BK_EN_8822B BIT(3)
#define BIT_LIFETIME_BE_EN_8822B BIT(2)
#define BIT_LIFETIME_VI_EN_8822B BIT(1)
#define BIT_LI