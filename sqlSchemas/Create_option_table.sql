USE [Trade]
GO

/****** Object:  Table [dbo].[OptionChain]    Script Date: 6/17/2020 5:02:57 AM ******/
DROP TABLE [dbo].[OptionChain]
GO

/****** Object:  Table [dbo].[OptionChain]    Script Date: 6/17/2020 5:02:57 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[OptionChain](
	[underlying] [varchar](100) NOT NULL,
	[strikePrice] [float] NOT NULL,
	[expiryDate] [date] NOT NULL,
	[DownloadDate] [date] NOT NULL,
	[OptionType] [varchar](2) NOT NULL,
	[identifier] [varchar](100) NULL,
	[openInterest] [int] NULL,
	[changeinOpenInterest] [float] NULL,
	[pchangeinOpenInterest] [float] NULL,
	[totalTradedVolume] [int] NULL,
	[impliedVolatility] [float] NULL,
	[lastPrice] [float] NULL,
	[change] [float] NULL,
	[pChange] [float] NULL,
	[totalBuyQuantity] [int] NULL,
	[totalSellQuantity] [int] NULL,
	[bidQty] [int] NULL,
	[bidprice] [float] NULL,
	[askQty] [int] NULL,
	[askPrice] [float] NULL,
	[underlyingValue] [float] NULL,
 CONSTRAINT [PK_OptionChain] PRIMARY KEY CLUSTERED 
(
	[underlying] ASC,
	[strikePrice] ASC,
	[expiryDate] ASC,
	[DownloadDate] ASC,
	[OptionType] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


