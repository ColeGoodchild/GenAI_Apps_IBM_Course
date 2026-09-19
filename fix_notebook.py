{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "944beac3-67cf-4d9f-bcb9-892fc204c16b",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: '-f'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mFileNotFoundError\u001b[39m                         Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 8\u001b[39m\n\u001b[32m      5\u001b[39m filename = sys.argv[\u001b[32m1\u001b[39m]\n\u001b[32m      6\u001b[39m output_filename = filename.replace(\u001b[33m\"\u001b[39m\u001b[33m.ipynb\u001b[39m\u001b[33m\"\u001b[39m, \u001b[33m\"\u001b[39m\u001b[33m_fixed.ipynb\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mfilename\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mr\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mutf-8\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[32m      9\u001b[39m     notebook = json.load(f)\n\u001b[32m     11\u001b[39m \u001b[38;5;28;01mfor\u001b[39;00m cell \u001b[38;5;129;01min\u001b[39;00m notebook[\u001b[33m\"\u001b[39m\u001b[33mcells\u001b[39m\u001b[33m\"\u001b[39m]:\n\u001b[32m     12\u001b[39m \n\u001b[32m     13\u001b[39m     \u001b[38;5;66;03m# Markdown cells should not contain outputs\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:327\u001b[39m, in \u001b[36m_modified_open\u001b[39m\u001b[34m(file, *args, **kwargs)\u001b[39m\n\u001b[32m    320\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[32m0\u001b[39m, \u001b[32m1\u001b[39m, \u001b[32m2\u001b[39m}:\n\u001b[32m    321\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[32m    322\u001b[39m         \u001b[33mf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mIPython won\u001b[39m\u001b[33m'\u001b[39m\u001b[33mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m by default \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    323\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    324\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33myou can use builtins\u001b[39m\u001b[33m'\u001b[39m\u001b[33m open.\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m    325\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m327\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mio_open\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfile\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[31mFileNotFoundError\u001b[39m: [Errno 2] No such file or directory: '-f'"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import nbformat\n",
    "import sys\n",
    "\n",
    "filename = sys.argv[1]\n",
    "output_filename = filename.replace(\".ipynb\", \"_fixed.ipynb\")\n",
    "\n",
    "with open(filename, \"r\", encoding=\"utf-8\") as f:\n",
    "    notebook = json.load(f)\n",
    "\n",
    "for cell in notebook[\"cells\"]:\n",
    "\n",
    "    # Markdown cells should not contain outputs\n",
    "    if cell[\"cell_type\"] == \"markdown\":\n",
    "        cell.pop(\"outputs\", None)\n",
    "        cell.pop(\"execution_count\", None)\n",
    "\n",
    "    # Code cells need valid execution_count and outputs\n",
    "    elif cell[\"cell_type\"] == \"code\":\n",
    "\n",
    "        if \"execution_count\" not in cell:\n",
    "            cell[\"execution_count\"] = None\n",
    "\n",
    "        outputs = cell.get(\"outputs\")\n",
    "\n",
    "        # Remove common invalid placeholder output\n",
    "        if outputs == [\"...0 outputs...\"] or not isinstance(outputs, list):\n",
    "            cell[\"outputs\"] = []\n",
    "\n",
    "# Convert to a proper notebook\n",
    "nb = nbformat.from_dict(notebook)\n",
    "\n",
    "# Validate before saving\n",
    "nbformat.validate(nb)\n",
    "\n",
    "with open(output_filename, \"w\", encoding=\"utf-8\") as f:\n",
    "    nbformat.write(nb, f)\n",
    "\n",
    "print(f\"✅ Fixed notebook: {output_filename}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
