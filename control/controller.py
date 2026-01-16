# control/controller.py

class DifferentialController:
    def __init__(
        self,
        v_nominal=0.8,
        v_min=0.1,
        v_max=1.2,
        omega_max=2.0,
        k_curvature=1.0,
        slowdown_gain=1.5
    ):
        """
        v_nominal     : kecepatan normal
        v_min, v_max  : batas kecepatan linear
        omega_max     : batas kecepatan sudut
        k_curvature   : gain kurvatur → omega
        slowdown_gain : pengaruh tikungan ke v
        """

        self.v_nominal = v_nominal
        self.v_min = v_min
        self.v_max = v_max
        self.omega_max = omega_max
        self.k_curvature = k_curvature
        self.slowdown_gain = slowdown_gain

    def compute_control(self, curvature):
        """
        Input : curvature (dari Pure Pursuit)
        Output: v, omega
        """

        # Angular velocity
        omega = self.k_curvature * curvature * self.v_nominal

        # Batasi omega
        omega = max(-self.omega_max, min(self.omega_max, omega))

        # Kurangi kecepatan saat tikungan tajam
        v = self.v_nominal / (1 + self.slowdown_gain * abs(curvature))

        # Batasi v
        v = max(self.v_min, min(self.v_max, v))

        return v, omega
