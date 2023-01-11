import streamlit as st


def _unsafe_md(markdown_text, component=st):
    component.markdown(markdown_text, unsafe_allow_html=True)


# ---- CSS


def local_css(file_name, component=st):
    with open(file_name) as f:
        _unsafe_md(f"<style>{f.read()}</style>", component)


def remove_streamlit_menu():
    _unsafe_md("<style>#MainMenu, footer, header {visibility: hidden;}</style>")


# ---- HTML


def spacer(height=1, component=st):
    _unsafe_md(f"<div style='height:{1 * height + 1}rem'></div>", component)


def div(component, _class="", text="", **kwargs):
    attributes = " ".join(f"{attr}='{value}'" for attr, value in kwargs.items())
    _unsafe_md(f"<div class='{_class}' {attributes}>{text}</div>", component)
