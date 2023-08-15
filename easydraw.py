{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMfrUaPlzOsdt16qKBgvBgn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/raymondWWW/CSC306_Fall2023/blob/main/easydraw.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kYUD3ZAA_WNE",
        "outputId": "765f49a2-d572-4430-c7c7-8e59f0e914ec"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: drawSvg==1.2.2 in /usr/local/lib/python3.10/dist-packages (1.2.2)\n",
            "Requirement already satisfied: numpy==1.21.1 in /usr/local/lib/python3.10/dist-packages (1.21.1)\n",
            "Requirement already satisfied: cairoSVG in /usr/local/lib/python3.10/dist-packages (from drawSvg==1.2.2) (2.7.1)\n",
            "Requirement already satisfied: imageio in /usr/local/lib/python3.10/dist-packages (from drawSvg==1.2.2) (2.31.1)\n",
            "Requirement already satisfied: cairocffi in /usr/local/lib/python3.10/dist-packages (from cairoSVG->drawSvg==1.2.2) (1.6.1)\n",
            "Requirement already satisfied: cssselect2 in /usr/local/lib/python3.10/dist-packages (from cairoSVG->drawSvg==1.2.2) (0.7.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.10/dist-packages (from cairoSVG->drawSvg==1.2.2) (0.7.1)\n",
            "Requirement already satisfied: pillow in /usr/local/lib/python3.10/dist-packages (from cairoSVG->drawSvg==1.2.2) (9.4.0)\n",
            "Requirement already satisfied: tinycss2 in /usr/local/lib/python3.10/dist-packages (from cairoSVG->drawSvg==1.2.2) (1.2.1)\n",
            "Requirement already satisfied: cffi>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from cairocffi->cairoSVG->drawSvg==1.2.2) (1.15.1)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.10/dist-packages (from cssselect2->cairoSVG->drawSvg==1.2.2) (0.5.1)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.1.0->cairocffi->cairoSVG->drawSvg==1.2.2) (2.21)\n"
          ]
        }
      ],
      "source": [
        "# Just a wrapper for drawSVG that uses global variables so that things are simplified a bit\n",
        "!pip install drawSvg==1.2.2 numpy==1.21.1\n",
        "\n",
        "import drawSvg as dSVG\n",
        "\n",
        "def easydraw(*args,**kwargs):\n",
        "    global drawSVG_easydraw\n",
        "    drawSVG_easydraw = dSVG.Drawing(*args, **kwargs)\n",
        "\n",
        "def Text(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Text(*args, **kwargs))\n",
        "\n",
        "def Rectangle(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Rectangle(*args, **kwargs))\n",
        "\n",
        "def Circle(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Circle(*args, **kwargs))\n",
        "\n",
        "def Ellipse(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Ellipse(*args, **kwargs))\n",
        "\n",
        "def ArcLine(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.ArcLine(*args, **kwargs))\n",
        "\n",
        "def Path(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Path(*args, **kwargs))\n",
        "\n",
        "def Lines(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Lines(*args, **kwargs))\n",
        "\n",
        "def Line(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Line(*args, **kwargs))\n",
        "\n",
        "def Arc(*args, **kwargs):\n",
        "    drawSVG_easydraw.append(dSVG.Arc(*args, **kwargs))\n",
        "\n",
        "def show_me_my_drawing():\n",
        "    return drawSVG_easydraw\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "E2RTgm-DAHS7"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
