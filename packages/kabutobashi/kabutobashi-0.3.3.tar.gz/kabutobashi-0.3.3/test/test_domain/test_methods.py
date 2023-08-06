import pytest

import kabutobashi as kb


@pytest.fixture(scope="module", autouse=True)
def sdsc() -> kb.StockDataSingleCode:
    sdmc = kb.example()
    sdsc = sdmc.to_single_code(code="1375")
    yield sdsc


def test_example_data(sdsc):
    columns = sdsc.df.columns
    assert "dt" in columns
    assert "open" in columns
    assert "close" in columns
    assert "high" in columns
    assert "low" in columns


def test_analysis_with_sma(sdsc):
    processed = sdsc.to_processed([kb.sma])
    columns = processed.processed[0].df.columns
    assert "sma_short" in columns
    assert "sma_medium" in columns
    assert "sma_long" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns

    processed.get_impact()


def test_analysis_with_macd(sdsc):
    processed = sdsc.to_processed([kb.macd])
    columns = processed.processed[0].df.columns
    assert "ema_short" in columns
    assert "ema_long" in columns
    assert "signal" in columns
    assert "macd" in columns
    assert "histogram" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


def test_analysis_with_stochastics(sdsc):
    processed = sdsc.to_processed([kb.stochastics])
    columns = processed.processed[0].df.columns
    assert "K" in columns
    assert "D" in columns
    assert "SD" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


def test_analysis_with_adx(sdsc):
    processed = sdsc.to_processed([kb.adx])
    columns = processed.processed[0].df.columns
    assert "plus_di" in columns
    assert "minus_di" in columns
    assert "DX" in columns
    assert "ADX" in columns
    assert "ADXR" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


@pytest.mark.skip(reason="buy_signal and sell_signal is not implemented")
def test_analysis_with_ichimoku(sdsc):
    processed = sdsc.to_processed([kb.ichimoku])
    columns = processed.processed[0].df.columns
    assert "line_change" in columns
    assert "line_base" in columns
    assert "proceding_span_1" in columns
    assert "proceding_span_2" in columns
    assert "delayed_span" in columns


def test_analysis_with_momentum(sdsc):
    processed = sdsc.to_processed([kb.momentum])
    columns = processed.processed[0].df.columns
    assert "momentum" in columns
    assert "sma_momentum" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


def test_analysis_with_psycho_logical(sdsc):
    processed = sdsc.to_processed([kb.psycho_logical])
    columns = processed.processed[0].df.columns
    assert "psycho_line" in columns
    assert "bought_too_much" in columns
    assert "sold_too_much" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


def test_analysis_with_bollinger_bands(sdsc):
    processed = sdsc.to_processed([kb.bollinger_bands])
    columns = processed.processed[0].df.columns
    assert "upper_2_sigma" in columns
    assert "lower_2_sigma" in columns
    assert "over_upper_continuity" in columns
    assert "over_lower_continuity" in columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


def test_analysis_with_fitting(sdsc):
    processed = sdsc.to_processed([kb.fitting])
    columns = processed.processed[0].df.columns
    assert "linear_fitting" in columns
    assert "square_fitting" in columns
    assert "cube_fitting" in columns


def test_analysis_with_basic(sdsc):
    processed = sdsc.to_processed([kb.basic])
    columns = processed.processed[0].df.columns
    assert "buy_signal" in columns
    assert "sell_signal" in columns


def test_get_impact_with(sdsc):
    result_1 = sdsc.to_processed(methods=[kb.sma])
    assert "sma" in [v.applied_method_name for v in result_1.processed]
    result_2 = sdsc.to_processed(methods=[kb.sma, kb.macd])
    assert "sma" in [v.applied_method_name for v in result_2.processed]
    assert "macd" in [v.applied_method_name for v in result_2.processed]
