import datetime as dt
import plotly.graph_objects as go


class CandlePlot:

    def __init__(self, df, candles=True):
        self.df_plot = df.copy()
        self.candles = candles
        self.create_candle_fig()

    def add_timestr(self):
        self.df_plot['sTime'] = [dt.datetime.strftime(x, "s%y-%m-%d %H:%M") for x in self.df_plot.time]


    def create_candle_fig(self):
        self.add_timestr()
        self.fig = go.Figure()
        if self.candles == True:
            self.fig.add_trace(go.Candlestick(
                x=self.df_plot.sTime,
                open=self.df_plot.mid_o,
                high=self.df_plot.mid_h,
                low=self.df_plot.mid_l,
                close=self.df_plot.mid_c,
                line=dict(width=1), opacity=1,
                increasing_fillcolor='#24a06b',
                decreasing_fillcolor='#cc2e35',
                increasing_line_color='#2ec886',
                decreasing_line_color='#ff3a4c'    
            ))

    def update_layout(self, width, height, nticks):
        self.fig.update_xaxes(
            gridcolor="#1f292f",
            rangeslider=dict(visible=False),
            nticks=nticks
        )

        self.fig.update_yaxes(
            gridcolor="#1f292f"    
            )
        # updating the layout of the plot
        self.fig.update_layout(
            width=width,
            height=height,
            margin=dict(l=10, r=10, b=10, t=10),
            paper_bgcolor="#2c303c",
            plot_bgcolor="#2c303c",
            font=dict(size=12, color="#e1e1e1")
        )

    def add_traces(self, line_traces):
        for t in line_traces:
            self.fig.add_trace(go.Scatter(
                x=self.df_plot.sTime,
                y=self.df_plot[t],
                line=dict(width=2),
                line_shape="spline",
                name=t
))


    def show_plot(self, width=1200, height=400, nticks=5, line_traces=[]):
        self.add_traces(line_traces)
        self.update_layout(width, height, nticks)
        self.fig.show()