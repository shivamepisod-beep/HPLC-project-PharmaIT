from src.data_loader import load_data 
from src.peak_detection import detect_peaks
from src.impurity_calc import calculate_impurity
from src.report import generate_report
import matplotlib.pyplot as plt

def main(): 
    file_path = "data/sample_hplc.csv" 

    data = load_data(file_path) 
    peaks = detect_peaks(data) 

    purity, impurity = calculate_impurity(peaks) 

    generate_report(peaks, purity, impurity)

    # Extract time and intensity for plotting
    time = data["time"]
    intensity = data["intensity"]
    peak_data = peaks

    # Smooth line
    plt.plot(time, intensity, linewidth=2)

    # Peak highlight + label
    for peak in peak_data:
        t, i = peak
        plt.scatter(t, i)

    plt.xlabel("Time (min)")
    plt.ylabel("Intensity")
    plt.title("HPLC Chromatogram")
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()
