22B)

#define BIT_SHIFT_NETYPE1_8822B 18
#define BIT_MASK_NETYPE1_8822B 0x3
#define BIT_NETYPE1_8822B(x)                                                   \
	(((x) & BIT_MASK_NETYPE1_8822B) << BIT_SHIFT_NETYPE1_8822B)
#define BIT_GET_NETYPE1_8822B(x)                                               \
	(((x) >> BIT_SHIFT_NETYPE1_8822B) & BIT_MASK_NETYPE1_8822B)

#define BIT_SHIFT_NETYPE0_8822B 16
#define BIT_MASK_NETYPE0_8822B 0x3
#define BIT_NETYPE0_8822B(x)                                                   \
	(((x) & BIT_MASK_NETYPE0_8822B) << BIT_SHIFT_NETYPE0_8822B)
#define BIT_GET_NETYPE0_8822B(x)                                               \
	(((x) >> BIT_SHIFT_NETYPE0_8822B) & BIT_MASK_NETYPE0_8822B)

#define BIT_I2C_MAILBOX_EN_8822B BIT(12)
#define BIT_SHCUT_EN_8822B BIT(11)
#define BIT_32K_CAL_TMR_EN_8822B BIT(10)
#define BIT_MAC_SEC_EN_8822B BIT(9)
#define BIT_ENSWBCN_8822B BIT(8)
#define BIT_MACRXEN_8822B BIT(7)
#define BIT_MACTXEN_8822B BIT(6)
#define BIT_SCHEDULE_EN_8822B BIT(5)
#define BIT_PROTOCOL_EN_8822B BIT(4)
#define BIT_RXDMA_EN_8822B BIT(3)
#define BIT_TXDMA_EN_8822B BIT(2)
#define BIT_HCI_RXDMA_EN_8822B BIT(1)
#define BIT_HCI_TXDMA_EN_8822B BIT(0)

/* 2 REG_PKT_BUFF_ACCESS_CTRL_8822B */

#define BIT_SHIFT_PKT_BUFF_ACCESS_CTRL_8822B 0
#define BIT_MASK_PKT_BUFF_ACCESS_CTRL_8822B 0xff
#define BIT_PKT_BUFF_ACCESS_CTRL_8822B(x)                                      \
	(((x) & BIT_MASK_PKT_BUFF_ACCESS_CTRL_8822B)                           \
	 << BIT_SHIFT_PKT_BUFF_ACCESS_CTRL_8822B)
#define BIT_GET_PKT_BUFF_ACCESS_CTRL_8822B(x)                                  \
	(((x) >> BIT_SHIFT_PKT_BUFF_ACCESS_CTRL_8822B) &                       \
	 BIT_MASK_PKT_BUFF_ACCESS_CTRL_8822B)

/* 2 REG_TSF_CLK_STATE_8822B */
#define BIT_TSF_CLK_STABLE_8822B BIT(15)

/* 2 REG_TXDMA_PQ_MAP_8822B */

#define BIT_SHIFT_TXDMA_HIQ_MAP_8822B 14
#define BIT_MASK_TXDMA_HIQ_MAP_8822B 0x3
#define BIT_TXDMA_HIQ_MAP_8822B(x)                                             \
	(((x) & BIT_MASK_TXDMA_HIQ_MAP_8822B) << BIT_SHIFT_TXDMA_HIQ_MAP_8822B)
#define BIT_GET_TXDMA_HIQ_MAP_8822B(x)                                         \
	(((x) >> BIT_SHIFT_TXDMA_HIQ_MAP_8822B) & BIT_MASK_TXDMA_HIQ_MAP_8822B)

#define BIT_SHIFT_TXDMA_MGQ_MAP_8822B 12
#define BIT_MASK_TXDMA_MGQ_MAP_8822B 0x3
#define BIT_TXDMA_MGQ_MAP_8822B(x)                                             \
	(((x) & BIT_MASK_TXDMA_MGQ_MAP_8822B) << BIT_SHIFT_TXDMA_MGQ_MAP_8822B)
#define BIT_GET_TXDMA_MGQ_MAP_8822B(x)                                         \
	(((x) >> BIT_SHIFT_TXDMA_MGQ_MAP_8822B) & BIT_MASK_TXDMA_MGQ_MAP_8822B)

#define BIT_SHIFT_TXDMA_BKQ_MAP_8822B 10
#define BIT_MASK_TXDMA_BKQ_MAP_8822B 0x3
#define BIT_TXDMA_BKQ_MAP_8822B(x)                                             \
	(((x) & BIT_MASK_TXDMA_BKQ_MAP_8822B) << BIT_SHIFT_TXDMA_BKQ_MAP_8822B)
#define BIT_GET_TXDMA_BKQ_MAP_8822B(x)                                         \
	(((x) >> BIT_SHIFT_TXDMA_BKQ_MAP_8822B) & BIT_MASK_TXDMA_BKQ_MAP_8822B)

#define BIT_SHIFT_TXDMA_BEQ_MAP_8822B 8
#define BIT_MASK_TXDMA_BEQ_MAP_8822B 0x3
#define BIT_TXDMA_BEQ_MAP_8822B(x)                                             \
	(((x) & BIT_MASK_TXDMA_BEQ_MAP_8822B) << BIT_SHIFT_TXDMA_BEQ_MAP_8822B)
#define BIT_GET_TXDMA_BEQ_MAP_8822B(x)                                         \
	(((x) >> BIT_SHIFT_TXDMA_BEQ_MAP_8822B) & BIT_MASK_TXDMA_BEQ_MAP_8822B)

#define BIT_SHIFT_TXDMA_VIQ_MAP_8822B 6
#define BIT_MASK_TXDMA_VIQ_MAP_8822B 0x3
#define BIT_TXDMA_VIQ_MAP_8822B(x)                                             \
	(((x) & BIT_MASK_TXDMA_VIQ_MAP_8822B) << BIT_SHIFT_TXDMA_VIQ_MAP_8822B)
#define BIT_GET_TXDMA_VIQ_MAP_8822B(x)                                         \
	(((x) >> BIT_SHIFT_TXDMA_VIQ_MAP_8822B) & BIT_MASK_TXDMA_VIQ_MAP_8822B)

#define BIT_SHIFT_TXDMA_VOQ_MAP_8822B 4
#define BIT_MASK_TXDMA_VOQ_MAP_8822B 0x3
#define BIT_TXDMA_VOQ_MAP_8822B(x)                                             \
	(((x) & BIT_MASK_TXDMA_VOQ_MAP_8822B) << BIT_SHIFT_TXDMA_VOQ_MAP_8822B)
#define BIT_GET_TXDMA_VOQ_MAP_8822B(x)                                         \
	(((x) >> BIT_SHIFT_TXDMA_VOQ_MAP_8822B) & BIT_MASK_TXDMA_VOQ_MAP_8822B)

#define BIT_RXDMA_AGG_EN_8822B BIT(2)
#define BIT_RXSHFT_EN_8822B BIT(1)
#define BIT_RXDMA_ARBBW_EN_8822B BIT(0)

/* 2 REG_TRXFF_BNDY_8822B */

#define BIT_SHIFT_RXFFOVFL_RSV_V2_8822B 8
#define BIT_MASK_RXFFOVFL_RSV_V2_8822B 0xf
#define BIT_RXFFOVFL_RSV_V2_8822B(x)                                           \
	(((x) & BIT_MASK_RXFFOVFL_RSV_V2_8822B)                                \
	 << BIT_SHIFT_RXFFOVFL_RSV_V2_8822B)
#define BIT_GET_RXFFOVFL_RSV_V2_8822B(x)                                       \
	(((x) >> BIT_SHIFT_RXFFOVFL_RSV_V2_8822B) &                            \
	 BIT_MASK_RXFFOVFL_RSV_V2_8822B)

#define BIT_SHIFT_TXPKTBUF_PGBNDY_8822B 0
#define BIT_MASK_TXPKTBUF_PGBNDY_8822B 0xff
#define BIT_TXPKTBUF_PGBNDY_8822B(x)                                           \
	(((x) & BIT_MASK_TXPKTBUF_PGBNDY_8822B)                                \
	 << BIT_SHIFT_TXPKTBUF_PGBNDY_8822B)
#define BIT_GET_TXPKTBUF_PGBNDY_8822B(x)                                       \
	(((x) >> BIT_SHIFT_TXPKTBUF_PGBNDY_8822B) &                            \
	 BIT_MASK_TXPKTBUF_PGBNDY_8822B)

/* 2 REG_PTA_I2C_MBOX_8822B */

/* 2 REG_NOT_VALID_8822B */

#define BIT_SHIFT_I2C_M_STATUS_8822B 8
#define BIT_MASK_I2C_M_STATUS_8822B 0xf
#define BIT_I2C_M_STATUS_8822B(x)                                              \
	(((x) & BIT_MASK_I2C_M_STATUS_8822B) << BIT_SHIFT_I2C_M_STATUS_8822B)
#define BIT_GET_I2C_M_STATUS_8822B(x)                                          \
	(((x) >> BIT_SHIFT_I2C_M_STATUS_8822B) & BIT_MASK_I2C_M_STATUS_8822B)

#define BIT_SHIFT_I2C_M_BUS_GNT_FW_8822B 4
#define BIT_MASK_I2C_M_BUS_GNT_FW_8822B 0x7
#define BIT_I2C_M_BUS_GNT_FW_8822B(x)                                          \
	(((x) & BIT_MASK_I2C_M_BUS_GNT_FW_8822B)                               \
	 << BIT_SHIFT_I2C_M_BUS_GNT_FW_8822B)
#define BIT_GET_I2C_M_BUS_GNT_FW_8822B(x)                                      \
	(((x) >> BIT_SHIFT_I2C_M_BUS_GNT_FW_8822B) &                           \
	 BIT_MASK_I2C_M_BUS_GNT_FW_8822B)

#define BIT_I2C_M_GNT_FW_8822B B