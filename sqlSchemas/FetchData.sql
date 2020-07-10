DECLARE @underlying varchar(100) = 'NIfty',
@optionType varchar(2) = 'CE', 
@expiryDate date = '2020-07-09'

if OBJECT_ID('tempdb..#topOption') is not null DROP TABLE tempdb..#topOption

select top 1  strikePrice, DownloadDate, underlyingValue
into #topOption
from OptionChain 
where 
underlying = @underlying
and OptionType = @optionType
and expiryDate = @expiryDate
and openInterest <>  0
order by DownloadDate desc, openInterest desc, changeinOpenInterest

select underlying, strikePrice, underlyingValue, DownloadDate, openInterest, changeinOpenInterest, lastPrice from OptionChain 
where underlying = @underlying
and OptionType = @optionType
and expiryDate = @expiryDate
and strikePrice = (select strikePrice from #topOption)

select SUM(openInterest) as 'Remainings calls before max call on current date' from OptionChain 
where underlying = @underlying
and OptionType = @optionType
and expiryDate = @expiryDate
and openInterest <>  0
and strikePrice  < (select strikePrice from #topOption)
and DownloadDate = (select DownloadDate from #topOption)


select SUM(openInterest) as 'Remainings calls before CMP on current date' from OptionChain 
where underlying = @underlying
and OptionType = @optionType
and expiryDate = @expiryDate
and openInterest <>  0
and strikePrice  <= (select underlyingValue from #topOption)
and DownloadDate = (select DownloadDate from #topOption)








