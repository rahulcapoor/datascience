USE [Trade]
GO

/****** Object:  StoredProcedure [dbo].[GetStockOptionChain]    Script Date: 6/20/2020 4:54:36 AM ******/
DROP PROCEDURE [dbo].[GetStockOptionChain]
GO

/****** Object:  StoredProcedure [dbo].[GetStockOptionChain]    Script Date: 6/20/2020 4:54:36 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE GetStockOptionChain @underlying varchar(100),  @optionType varchar(2), @expiryDate date
AS
select strikePrice, DownloadDate, openInterest, changeinOpenInterest, lastPrice, impliedVolatility, underlying, underlyingValue
from OptionChain
where 
underlying = @underlying
and OptionType = @optionType
and expiryDate = @expiryDate
and openInterest <>  0
order by DownloadDate desc, openInterest desc, changeinOpenInterest

GO


