from manim import *
import numpy as np
from math import *

config.background_color =  WHITE #  "#020416"
dark_red = "#9A0000"
light_red = "#9A000045"
dark_pink = "#9C1568"
light_pink = "#9C15686F"
dark_blue = "#336699"
medium_blue = "#7597BE"
light_blue = "#33669962"
dark_green = "#5E913B"
light_green = "#5D913B66"
dark_orange = "#E66914"
light_orange = "#E668149B"
dark_purple = "#5802A6"
light_purple = "#5702A68C"
dark_terquise = "#02A6A1"
dark_not_green = "#46A602"
axes_background_color = "#D3D3D3"
topics_backGround_color = "#020416"

class Part1_Scene(MovingCameraScene):
    #  Norm → Metric → Cauchy → Completeness → Banach
    #  Define Length → Create Distance → Chase Limits → Reach Completeness → Enter Banach
    topics = {
        0: "The Birth of Norms", #Norms on Vector Spaces
        1: "From Norms to Metrics", #How a Norm Generates a Metric?
        2: "Cauchy Sequences : The Mystery of Nearness", #What Does It Mean to Be Cauchy?  - Cauchy Sequences in Metric Spaces
        3: "Banach Spaces : The Kingdom of Completeness",
    }

    def auto_adjust_position(mobject, padding=0.5):
        frame_width = config.frame_width
        frame_height = config.frame_height
        
        shift_amount = np.array([0, 0, 0])
        
        if mobject.get_right()[0] > frame_width/2 - padding:
            overflow = mobject.get_right()[0] - (frame_width/2 - padding)
            shift_amount += LEFT * overflow
        
        if mobject.get_left()[0] < -frame_width/2 + padding:
            overflow = (-frame_width/2 + padding) - mobject.get_left()[0]
            shift_amount += RIGHT * overflow
        
        if mobject.get_top()[1] > frame_height/2 - padding:
            overflow = mobject.get_top()[1] - (frame_height/2 - padding)
            shift_amount += DOWN * overflow
        
        if mobject.get_bottom()[1] < -frame_height/2 + padding:
            overflow = (-frame_height/2 + padding) - mobject.get_bottom()[1]
            shift_amount += UP * overflow
        
        if np.any(shift_amount != 0):
            mobject.shift(shift_amount)
        
        return mobject

    def show_warning(self, body: MathTex,set_image=False,return_not_show=False):
        """Show warning message with box"""

        title_text = Text("❗Note❗", color=dark_red, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_red,
            fill_color=light_red,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )

        box.move_to(group.get_center())

        if set_image==True:
            # ex_mark_1 = ImageMobject("images/ex_mark_1_img.png").move_to(box.get_top()+ 3*LEFT + 1.5*UP ).scale(3)
            # self.add(ex_mark_1) 

            ex_mark_2 = ImageMobject("images/ex_mark_2_img.png").move_to(box.get_top()+ 1.5*UP ).scale(3)
            self.add(ex_mark_2)

            # arrow_0_0_down = CurvedArrow(
            #     start_point=box.get_corner(UR)+2*UP+1.5*LEFT,
            #     end_point=box.get_top()+1.0*RIGHT,
            #     angle=PI/2,
            #     color=light_red,
            # ).scale(1.5)
            # self.play(
            #     Create(arrow_0_0_down),
            #     run_time=1
            # )
        if return_not_show==False:
            self.play(Create(box), Write(group))
            self.wait(2)
            self.play(FadeOut(group), FadeOut(box))

        if set_image==True:
            self.play(
                # FadeOut(arrow_0_0_down),
                # FadeOut(ex_mark_1),
                FadeOut(ex_mark_2)
            )
        if return_not_show==True:
            return group, box

    def ask_question(self,body, return_notShow=False,set_image=False):
        """Show message with box to ask a question. """

        title_text = Text("🤔Question", color=dark_pink, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_pink,
            fill_color=light_pink,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            list_images = []
            if set_image==True:
                ex_mark_2 = ImageMobject("images/think_img.png").move_to(box.get_top()+ 0.1*UP ).scale(2.2)
                # self.add(ex_mark_2)
                self.wait(1)

                ex_mark_1 = ImageMobject("images/find_img.png").to_edge(DR).shift(0.5*LEFT).scale(2)
                # self.add(ex_mark_1)
                list_images+=[ex_mark_2, ex_mark_1]
            return group, box, *list_images
        
        if set_image==True:
            ex_mark_2 = ImageMobject("images/think_img.png").move_to(box.get_top()+ 0.1*UP ).scale(2)
            self.add(ex_mark_2)
            self.wait(1)

        self.play(Create(box), Write(group))

        self.wait(1)
        if set_image==True:
            ex_mark_1 = ImageMobject("images/find_img.png").to_edge(DR).shift(0.5*LEFT).scale(2)
            self.add(ex_mark_1)

        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))

        if set_image==True:
            self.play(
                FadeOut(ex_mark_2),
                FadeOut(ex_mark_1)
            )

    def show_minorPoint(self,body,return_notShow):
        """Show message with box to ask a question. """

        title_text = Text("Note", color=dark_blue, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_blue,
            fill_color=light_blue,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
        return group, box

    def show_definition(self, definition: MathTex, total_title, retrun_notShow=False, what_is_defined=""):
        """Show definition with box"""

        title_text = Text(f"⚙️📃Definition {what_is_defined}", color=dark_green, font_size=36)

        group = VGroup(title_text, definition).arrange(DOWN, buff=0.3)
        
        box = RoundedRectangle(
            corner_radius=0.3,
            color=dark_green,
            fill_color=light_green,
            fill_opacity=0.15,
            width=group.width + 1,
            height=group.height + 0.8
        )

        new_position = total_title.get_center() + DOWN * (box.height)
        group.move_to(new_position)
        if group.is_off_screen():
            self.auto_adjust_position(group)
        
        box.move_to(group.get_center())

        if box.is_off_screen():
            self.auto_adjust_position(box)
        
        if retrun_notShow :
            return group,box
        
        self.play(Create(box), Write(group))
        self.wait(2)
        return group, box
    
    def show_conclusion(self,total_title,body,return_notShow=False):
        """Show message with box to conclude some thing. """

        title_text = Text("Conclusion", color= dark_orange, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color= dark_orange,
            fill_color=light_orange,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
    
    def show_example(self,total_title,body,title_text_for_box,return_notShow=False):
        """Show message with box to show some examples. """

        title_text = Text(title_text_for_box, color= dark_purple, font_size=36)

        group = VGroup(title_text, body).arrange(DOWN, buff=0.3)

        box = RoundedRectangle(
            corner_radius=0.3,
            color= dark_purple,
            fill_color=light_purple,
            fill_opacity=0.2,
            width=group.width + 1,
            height=group.height + 0.8
        )
        

        box.move_to(group.get_center())

        if return_notShow :
            return group, box

        self.play(Create(box), Write(group))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(box))
    
    def construct(self):

        # self.scene1()

        # self.scene2()

        # the birth of norms
        # topic_number = 0
        # title = self.scene3(topic_number,False)

        # self.scene4(title)

        # from norm to metrics
        topic_number = 1
        title = self.scene3(topic_number,False)

        self.scene5(title)

        # Cauchy Sequences : The Mystery of Nearness
        # topic_number = 2
        # title = self.scene3(topic_number,False)

        # self.scene6(title)

        # Banach Spaces : The Kingdom of Completeness
        # topic_number = 3
        # title = self.scene3(topic_number,False)

        # self.scene7(title)

    def scene7_SubScene0(self, title):
        part1 = MathTex(
            r"\text{A Banach space is a normed space } (X,\|\cdot\|) ",
            # r"d(x,y)=\|x-y\|.",
            color=BLACK
        )
        part2 = MathTex(
            r"\text{ which is complete with respect to the metric}",
            # r"d(x,y)=\|x-y\|.",
            color=BLACK
        )
        part3 = MathTex(
            r"\text{induced by the norm .}",
            # r"d(x,y)=\|x-y\|.",
            color=BLACK
        )
        banach_definition = VGroup(part1, part2, part3).arrange(DOWN,buff=0.2)

        group, box = self.show_definition(banach_definition,title,True)
        banach_group = VGroup(group, box).scale(1.2)

        self.play(
            Create(box),
            Write(group),
        )

        self.wait(1)

        self.play(
            FadeOut(banach_group),
        )

    def scene7_SubScene1(self, title):
        ...

    def scene7(self, title):
        """ Banach Spaces : The Kingdom of Completeness """
        self.play(
            Write(title),
        )
        # self.wait(0.3)
        # self.play(
        #     FadeOut(title),
        # )
        # self.wait(1)

        # self.scene7_SubScene0(title)

        self.scene7_SubScene1(title)

    def scene6_subScene0(self, title):

        # part 1
        
        text_xn = MathTex(r"(X, d) \text{ Metric space, } ",r"(y_n)_{n \in \mathbb{N}} \subset X",color=BLACK).to_edge(UL)
        text_converge = Text("Convergent", color=BLACK).move_to(text_xn.get_center()+1.5*DOWN+2*LEFT)
        rect_converge = SurroundingRectangle(
            text_converge,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        converge_def = MathTex(r"\lim_{n \to \infty} y_n = y",r"\in X", color=BLACK).next_to(rect_converge, RIGHT,buff=0.5)

        self.play(
            Write(text_xn[0]),
        )
        self.wait(0.3)
        self.play(
            Write(text_xn[1]),
        )
        self.wait(0.5)
        self.play(
            Create(rect_converge),
            Write(text_converge),
        )
        self.wait(1)
        self.play(
            Write(converge_def[0]),
        )
        self.wait(0.5)
        self.play(
            Write(converge_def[1]),
        )
        self.wait(0.5)
        self.play(
            FadeOut(converge_def),
        )
        self.wait(0.5)

        # shape

        zoom = 3
        grid = NumberPlane(
            x_range=[-7, 7, 0.5], 
            y_range=[-5, 6, 0.5], 
            background_line_style={"stroke_opacity": 0.3, "stroke_color":axes_background_color},
            color=axes_background_color
        ) #.shift(DOWN)
        self.play(
            Create(grid),
        )
        axes = Axes(  # NumberLine
            x_range=[-7, 7, 0.5], 
            y_range=[-5, 6, 0.5],
            # axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        )
        shape_center = grid.get_center() + DOWN*0.5 + RIGHT*1

        angles = np.linspace(0, 2*PI, 8, endpoint=False)
        radii = [1.4, 1.3, 1.0, 1.5, 1.4, 1.2, 0.6, 1.5]
        radii = [r * zoom for r in radii]

        points = [
            shape_center + np.array([
                radii[i] * np.cos(angles[i]),
                radii[i] * np.sin(angles[i]),
                0
            ])
            for i in range(len(angles))
        ]

        smooth_shape = VMobject(color=dark_pink, fill_color=light_pink, fill_opacity=0.1)
        smooth_shape.set_points_smoothly(points + [points[0]])
        smooth_shape.close_path()
        smooth_shape.shift(1*RIGHT)

        text_x = Text("X",color=BLACK).next_to(smooth_shape,DOWN).shift(0.6*UP)

        self.play(
            Create(smooth_shape),
            Write(text_x),
            run_time=2
        )

        limit_dot = Dot(axes.c2p(5.5,-3.5),color=dark_red, radius=0.08).shift(0.3*DR)
        text_y_limit = MathTex(r"y",color=BLACK).next_to(limit_dot, UP, buff=0.2)
        limit_text = Text("limit", font_size=24, color=BLACK, weight=BOLD)
        limit_text.next_to(limit_dot, UP, buff=0.3)
        self.play(
            Create(limit_dot),
            Write(text_y_limit),
        )

        points = [
            axes.c2p(-2,4),
            axes.c2p(1,1),
            axes.c2p(3,-1),
            axes.c2p(4,-2),
            axes.c2p(4.5,-2.5),
            axes.c2p(4.75,-2.75),
        ]
        dots = []
        text_xi = []
        for i,p in enumerate(points):
            dots.append( 
                new_dot:=Dot(p, color=dark_blue, radius=0.08).shift(0.3*DR)
            )
            if i%2==0:
                text_xi.append(
                    new_text:=MathTex(rf"y_{i+1}",color=BLACK).scale(0.7).next_to(new_dot,UP)
                )
            else:
                text_xi.append(
                    new_text:=MathTex(rf"y_{i+1}",color=BLACK).scale(0.7).next_to(new_dot,DOWN)
                )
            
            line = Line(
                start=new_dot.get_center(),
                end=limit_dot.get_center(),
                color=dark_green,
                stroke_width=2,
            )

            self.play(
                FadeIn(new_dot),
                Write(new_text),
            )
            self.wait(0.1)
            self.play(
                Create(line)
            )
            self.wait(0.1)
            self.play(
                Uncreate(line)
            )
        
        dots_group = VGroup(*dots)
        text_xi_group = VGroup(*text_xi)

        arrow = Arrow(
            start=dots[-1].get_center(),
            end=limit_dot.get_center(),
            color=BLACK,
            stroke_width=4,
            tip_length=0.15,
            tip_shape=StealthTip,
        )

        final_dot = Dot(
            point=limit_dot.get_center(),
            color=BLACK,
            radius=0.12,
            fill_opacity=1
        )

        self.play(
            GrowArrow(arrow),
            FadeTransform(text_y_limit, limit_text),
            Transform(limit_dot, final_dot),
        )

        for _ in range(2):
            self.play(
                final_dot.animate.scale(1.5).set_color(dark_red),
                rate_func=there_and_back,
            )
        
        self.wait(1)

        # part 2

        smooth_shape_copy = smooth_shape.copy().set_color(dark_orange).scale(0.85).shift(0.45*UL)
        text_y = Text("Y",color=BLACK).next_to(smooth_shape_copy,RIGHT) #.shift(0.4*DOWN)
        self.play(
            FadeOut(arrow),
            TransformFromCopy(smooth_shape, smooth_shape_copy),
            Write(text_y),
            run_time=1
        )

        cross_img = ImageMobject("images/red_cross.png").scale(2).move_to(text_converge)
        self.add(cross_img)
        self.wait(2)
        self.play(
            FadeOut(cross_img),
        )
        prop = MathTex(
            r"\text{Properties of}\\ \text{the sequence}",
            color=BLACK
        )

        plus = MathTex(
            r"+",
            color=BLACK
        )

        space = MathTex(
            r"\text{Underlying }\\ \text{metric space}",
            color=BLACK
        )

        text_explain = VGroup(prop, plus, space).arrange(DOWN, buff=0.5).next_to(rect_converge, DOWN,buff=0.3)
        rect_text_expalin = SurroundingRectangle(
            text_explain,
            color=dark_green,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        self.play(
            Create(rect_text_expalin),
            Write(text_explain),
        )
        self.wait(0.5)
        space.set_color(dark_red)
        self.wait(0.5)

        fade_out_list = [
            rect_text_expalin, text_explain, text_converge, rect_converge, text_xn, grid,
            smooth_shape, text_x, limit_dot, limit_text, dots_group, text_xi_group, 
            final_dot, smooth_shape_copy, text_y,
        ]

        self.wait(1)
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )
        self.wait(1)


    def scene6_subScene1(self, title):
        
        # come_up_img = ImageMobject("come up with.png").scale(3).to_edge(UP)
        # self.add(come_up_img)

        question = MathTex(r"\text{How can we define a space-independent idea of convergence?}",color=BLACK).scale(0.9)
        group, box, think_img, find_img = self.ask_question(question,True,True)

        group_GroupBoxQuetion = VGroup(group, box)
        group_GroupBoxQuetion.shift(2*UP)
        think_img.scale(1.2).shift(2.8*DOWN)
        self.add(think_img)
        self.wait(0.2)
        self.play(
            FadeIn(group_GroupBoxQuetion),
        )
        self.wait(1)

        fade_out_list = [
            group_GroupBoxQuetion
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
            FadeOut(think_img),
        )
    
    def scene6_subScene2(self, title):

        title_cauchy_text = Tex("Cauchy sequence", color=BLACK, font_size=80).move_to(title.get_center())
        self.play(
            Write(title_cauchy_text),
        )
        
        part0 = MathTex(r"A\ sequence\ \{x_n\}\ in\ a\ metric\ space\ (X,d)\ ",color=BLACK) #(or fundamental)
        part0_to_1 = MathTex(r"\Longleftrightarrow",color=BLACK)
        part1 = MathTex(r"\text{is said to be Cauchy if } \text{for every } \varepsilon > 0,",color=BLACK)
        part2 = MathTex(r"\text{there exists } N = N(\varepsilon) \text{ such that}",color=BLACK)
        part3 = MathTex(r"d(x_m,x_n) < \varepsilon ",color=BLACK)
        part4 = MathTex(r"\text{for every } m,n > N",color=BLACK)
        # part1 = MathTex(r"\forall \varepsilon > 0,")
        # part2 = MathTex(r"\exists N \in \mathbb{N}")
        # part3 = MathTex(r"\forall m,n \ge N,")
        # part4 = MathTex(r"d(x_m,x_n) < \varepsilon")

        definition_part1 = VGroup(part0,part1, part2, part3, part4).arrange(DOWN, buff=0.2)

        group, box = self.show_definition(definition_part1,title,True)
        def_group = VGroup(group,box).scale(1.2).shift(1*UP)
        self.play(
            FadeIn(def_group),
        )
        self.wait(1)
        self.play(
            FadeOut(def_group),
            # FadeOut(def_group),
        )
        self.wait(1)

        return title_cauchy_text

    def scene6_subScene3(self, title, title_cauchy_text):
        
        zoom = 3
        grid = NumberPlane(
            x_range=[-7, 7, 0.5], 
            y_range=[-5, 6, 0.5], 
            background_line_style={"stroke_opacity": 0.3, "stroke_color":axes_background_color},
            color=axes_background_color
        ) #.shift(DOWN)
        self.play(
            Create(grid),
        )
        axes = Axes(  # NumberLine
            x_range=[-7, 7, 0.5], 
            y_range=[-5, 6, 0.5],
            # axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        )
        shape_center = grid.get_center() + DOWN*0.5 + RIGHT*1

        angles = np.linspace(0, 2*PI, 8, endpoint=False)
        radii = [1.4, 1.3, 1.0, 1.5, 1.4, 1.2, 0.6, 1.5]
        radii = [r * zoom for r in radii]

        points = [
            shape_center + np.array([
                radii[i] * np.cos(angles[i]),
                radii[i] * np.sin(angles[i]),
                0
            ])
            for i in range(len(angles))
        ]

        smooth_shape = VMobject(color=dark_pink, fill_color=light_pink, fill_opacity=0.1)
        smooth_shape.set_points_smoothly(points + [points[0]])
        smooth_shape.close_path()
        smooth_shape.shift(1*RIGHT)
        smooth_shape_copy = smooth_shape.copy().set_color(dark_orange).scale(0.9).shift(0.2*DL + LEFT*0.2)
        text_y = Text("Y",color=BLACK).next_to(smooth_shape_copy,RIGHT) #.shift(0.4*DOWN)
        self.play(
            Create(smooth_shape_copy),
            Write(text_y),
            run_time=1
        )

        points = [
            axes.c2p(-2,4),
            axes.c2p(1,1),
            axes.c2p(3,-1),
            axes.c2p(4,-2),
            axes.c2p(4.5,-2.5),
            axes.c2p(4.75,-2.75),
        ]
        dots = []
        text_xi = []
        old_dot = None
        for i,p in enumerate(points):
            dots.append( 
                new_dot:=Dot(p, color=dark_blue, radius=0.08).shift(0.5*DR)
            )
            if i%2==0:
                text_xi.append(
                    new_text:=MathTex(rf"y_{i+1}",color=BLACK).scale(0.7).next_to(new_dot,UP)
                )
            else:
                text_xi.append(
                    new_text:=MathTex(rf"y_{i+1}",color=BLACK).scale(0.7).next_to(new_dot,DOWN)
                )

            self.play(
                FadeIn(new_dot),
                Write(new_text),
            )

            if i!=0:
                line = Line(
                    start=old_dot.get_center(),
                    end=new_dot.get_center(),
                    color=dark_green,
                    stroke_width=2,
                )

                self.play(
                    Create(line)
                )
                # self.wait(0.1)
                self.play(
                    Uncreate(line)
                )
            
            old_dot = new_dot
        
        dots_group = VGroup(*dots)
        text_xi_group = VGroup(*text_xi)
        
        self.wait(1)

        prop = MathTex(
            r"\text{Intrinsic property}\\ \text{of the sequence }",
            color=BLACK
        )

        but = MathTex(
            r"\text{But}",
            color=BLACK
        )

        space = MathTex(
            r"\text{Independent}\\",
            r"\text{of the space}",
            color=BLACK
        )

        text_explain = VGroup(prop, but, space).arrange(DOWN, buff=0.5).next_to(smooth_shape_copy, LEFT,buff=0.5).scale(0.9)
        rect_text_expalin = SurroundingRectangle(
            text_explain,
            color=dark_green,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Create(rect_text_expalin),
            Write(text_explain),
        )
        self.wait(1)
        space[0].set_color(dark_red)
        self.wait(1)

        fade_out_list = [
            title_cauchy_text , grid, smooth_shape_copy, dots_group, text_xi_group, text_y, text_explain,
            rect_text_expalin,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )
        self.wait(1)

        # lines = VGroup()
        # for i in range(len(points)-1):
        #     line = Line(
        #         start=points[i],
        #         end=points[i+1],
        #         color=dark_green,
        #         stroke_width=2,
        #     ).shift(0.4*DR)
        #     lines.add(line)

        # self.play(Create(lines), run_time=2)
        # self.wait(0.5)
        # self.play(FadeOut(lines))

    def scene6_subScene4(self, title):

        book_brain_img = ImageMobject("images/book_brain.png").scale(1.5).to_corner(DL).shift(0.3*DL)
        self.add(book_brain_img)

        convergent_implies_cauchy = MathTex(
            r"\text{Convergent} \;\Rightarrow\; \text{Cauchy}",color=BLACK
        ).to_corner(UL)
        
        cauchy_not_implies_convergent = MathTex(
            r"\text{Cauchy} \;\not\Rightarrow\; \text{Convergent} \;",
            color=BLACK  #r"(\text{limit may not exist in the space})",
        ).next_to(convergent_implies_cauchy, DOWN, buff=0.8)
        
        counter_example = MathTex(
            r"x_n = 1 - \frac{1}{n} \in (0,1), \quad n=1,2,\dots",color=BLACK
        ).next_to(cauchy_not_implies_convergent, DOWN, buff=0.6)
        limit_counter_example = MathTex(
            r"\quad \lim_{n\to\infty} x_n = 1 \notin (0,1)",color=BLACK
        ).next_to(counter_example, DOWN, buff=0.6)

        group, box = self.show_minorPoint(convergent_implies_cauchy,True)
        con_to_cach = VGroup(box, group).to_corner(UL).scale(0.9)
        

        zoom = 3
        # -------------------- Grid & Axes --------------------
        grid = NumberPlane(
            x_range=[-9, 9, 0.5], 
            y_range=[-5, 6, 0.5], 
            background_line_style={
                "stroke_opacity": 0.3,
                "stroke_color": axes_background_color
            },
            color=axes_background_color
        )

        axes = Axes(
            x_range=[-9, 9, 0.5], 
            y_range=[-5, 6, 0.5],
        )

        # -------------------- Smooth Shape X --------------------
        shape_center = grid.get_center() + DOWN*0.5 + RIGHT*1

        angles = np.linspace(0, 2*PI, 8, endpoint=False)
        radii = [1.4, 1.3, 1.0, 1.5, 1.4, 1.2, 0.6, 1.5]
        radii = [r * zoom for r in radii]

        points_shape = [
            shape_center + np.array([
                radii[i] * np.cos(angles[i]),
                radii[i] * np.sin(angles[i]),
                0
            ])
            for i in range(len(angles))
        ]

        smooth_shape = VMobject(
            color=dark_pink,
            fill_color=light_pink,
            fill_opacity=0.1
        )
        smooth_shape.set_points_smoothly(points_shape + [points_shape[0]])
        smooth_shape.close_path()
        smooth_shape.shift(1*RIGHT)

        text_x = Text("X", color=BLACK).next_to(smooth_shape, DOWN).shift(0.6*UP)

        # -------------------- Limit Point --------------------
        limit_dot = Dot(
            axes.c2p(5.5, -3.5),
            color=BLACK,
            radius=0.12
        ).shift(0.3*DR)

        limit_text = Text("limit", font_size=24, color=BLACK, weight=BOLD)
        limit_text.next_to(limit_dot, UP, buff=0.3)

        # -------------------- Sequence Points --------------------
        points_seq = [
            axes.c2p(-2,4),
            axes.c2p(1,1),
            axes.c2p(3,-1),
            axes.c2p(4,-2),
            axes.c2p(4.5,-2.5),
            axes.c2p(4.75,-2.75),
        ]

        dots = []
        text_xi = []

        for i, p in enumerate(points_seq):

            new_dot = Dot(p, color=dark_blue, radius=0.08).shift(0.3*DR)
            dots.append(new_dot)

            if i % 2 == 0:
                label = MathTex(rf"y_{i+1}", color=BLACK).scale(0.7).next_to(new_dot, UP)
            else:
                label = MathTex(rf"y_{i+1}", color=BLACK).scale(0.7).next_to(new_dot, DOWN)

            text_xi.append(label)

        # -------------------- Arrow --------------------
        arrow = Arrow(
            start=dots[-1].get_center(),
            end=limit_dot.get_center(),
            color=BLACK,
            stroke_width=4,
            tip_length=0.15,
            tip_shape=StealthTip,
        )

        # -------------------- Shape Y --------------------
        smooth_shape_copy = smooth_shape.copy()
        smooth_shape_copy.set_color(dark_orange)
        smooth_shape_copy.scale(0.85)
        smooth_shape_copy.shift(0.45*UL)

        text_y = Text("Y", color=BLACK).next_to(smooth_shape_copy, RIGHT)

        # -------------------- Group Everything --------------------
        all_objects = VGroup(
            smooth_shape,
            text_x,
            limit_dot,
            limit_text,
            *dots,
            *text_xi,
            arrow,
            smooth_shape_copy,
            text_y,
        )

        all_objects.scale(0.85).shift(0.5*DOWN+0.3*RIGHT)

        self.play(
            FadeIn(grid),
            FadeIn(all_objects),
        )
        self.play(
            Create(box),
            Write(group),
        )

        self.wait(2)
        self.play(
            FadeOut(con_to_cach),
            FadeOut(all_objects),
        )
        self.wait(0.5)
        group, box = self.show_warning(cauchy_not_implies_convergent,False,True)
        cha_to_con = VGroup(box, group).to_edge(UP)
        self.play(
            Create(box),
            Write(group),
            run_time=1
        )
        self.wait(1)

        example_group = VGroup(counter_example, limit_counter_example).arrange(DOWN, buff=0.5)
        group, box = self.show_example(title, example_group,"Counterexample",True)
        example_group_box = VGroup(box, group).next_to(cha_to_con, DOWN, buff=0.8) #.shift(1.5*RIGHT)

        self.play(
            Create(box),
            Write(group),
            run_time=1
        )
        self.wait(1)

        fade_out_list = [
            cha_to_con, example_group_box,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
            FadeOut(book_brain_img),
        )
        self.play(
            FadeOut(grid),
        )
        self.wait(1)

    def scene6_subScene5(self, title):
        book_brain_img = ImageMobject("images/find_img.png").scale(1.7).to_corner(DL).shift(0.3*DL+3*LEFT+UP*4)
        book_brain_img.rotate(180*DEGREES)
        self.add(book_brain_img)

        self.wait(1)

        final_note_1 = MathTex(
            r"\text{Let us build a space where}",color=BLACK
        ).scale(1.5)
        final_note_2 = MathTex(r"\text{Convergent} \;\Leftrightarrow\; \text{Cauchy}",color=BLACK
        ).scale(1.5)
        final_note = VGroup(final_note_1, final_note_2).arrange(DOWN,buff=0.3)

        tot_title = MathTex(r"IDEA",color=dark_purple).scale(2)
        group, box = self.show_example(title,final_note,"IDEA",True)
        final_group = VGroup(group, box).shift(0.5*DOWN)

        self.play(
            Create(box),
            Write(group),
        )
        self.wait(0.5)
        self.play(
            FadeOut(final_group),
        )

        title_compelte_text = Tex("Complete Space", color=BLACK, font_size=80).move_to(title.get_center())
        self.play(
            Write(title_compelte_text),
        )
        self.wait(1)

        part1 = MathTex(
            r"A\ metric\ space\ (X,d)\ \text{is said to be complete if}", 
            color=BLACK
        )
        part2 = MathTex(
            r"\text{every Cauchy sequence } \{x_n\} \subset X,",
            color=BLACK
        )
        part3 = MathTex(
            r"\text{converges, i.e., there exists } x \in X \text{ such that}",
            color=BLACK
        )
        part4 = MathTex(
            r"\lim_{n \to \infty} x_n = x",
            color=BLACK
        )
        complete_def = VGroup(part1, part2, part3, part4).arrange(DOWN,buff=0.3)
        group, box = self.show_definition(complete_def,title_compelte_text,True)
        def_group = VGroup(group, box).scale(1.2).shift(0.5*UP)

        self.play(
            Create(box),
            Write(group),
            run_time=1
        )
        self.wait(1)

        fade_out_list = [
            group, box, title_compelte_text
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
            FadeOut(book_brain_img),
        )

        self.wait(1)

    def scene6(self, title):
        """ Cauchy Sequences : The Mystery of Nearness """
        title.shift(0.3*DOWN)
        # self.play(
        #     Write(title),
        # )
        # self.wait(1)
        # self.play(
        #     FadeOut(title),
        # )
        # self.wait(0.5)

        # Recall Convergence
        # self.scene6_subScene0(title)

        # Intuitive Idea
        # self.scene6_subScene1(title)

        # Formal Definition of Cauchy
        # title_cauchy_text = self.scene6_subScene2(title)

        # Intuitive Idea of Cauchy
        # self.scene6_subScene3(title, title_cauchy_text)

        ## ( Convergence <-> Cauchy ) & Question
        self.scene6_subScene4(title)

        # Formal Definition of Completeness
        # self.scene6_subScene5(title)

        # complete intuition with shapes
        # self.scene6_subScene6(title)


    def scene6_subScene6(self, title):
        zoom = 3
        # -------------------- Grid & Axes --------------------
        grid = NumberPlane(
            x_range=[-7, 7, 0.5], 
            y_range=[-5, 6, 0.5], 
            background_line_style={
                "stroke_opacity": 0.3,
                "stroke_color": axes_background_color
            },
            color=axes_background_color
        )

        axes = Axes(
            x_range=[-7, 7, 0.5], 
            y_range=[-5, 6, 0.5],
        )

        # -------------------- Smooth Shape X --------------------
        shape_center = grid.get_center() + DOWN*0.5 + RIGHT*1

        angles = np.linspace(0, 2*PI, 8, endpoint=False)
        radii = [1.4, 1.3, 1.0, 1.5, 1.4, 1.2, 0.6, 1.5]
        radii = [r * zoom for r in radii]

        points_shape = [
            shape_center + np.array([
                radii[i] * np.cos(angles[i]),
                radii[i] * np.sin(angles[i]),
                0
            ])
            for i in range(len(angles))
        ]

        smooth_shape = VMobject(
            color=dark_pink,
            fill_color=light_pink,
            fill_opacity=0.1
        )
        smooth_shape.set_points_smoothly(points_shape + [points_shape[0]])
        smooth_shape.close_path()
        smooth_shape.shift(1*RIGHT)

        text_x = Text("X", color=BLACK).next_to(smooth_shape, DOWN).shift(0.6*UP)

        # -------------------- Limit Point --------------------
        limit_dot = Dot(
            axes.c2p(5.5, -3.5),
            color=BLACK,
            radius=0.12
        ).shift(0.3*DR)

        limit_text = Text("limit", font_size=24, color=BLACK, weight=BOLD)
        limit_text.next_to(limit_dot, UP, buff=0.3)

        # -------------------- Sequence Points --------------------
        points_seq = [
            axes.c2p(-2,4),
            axes.c2p(1,1),
            axes.c2p(3,-1),
            axes.c2p(4,-2),
            axes.c2p(4.5,-2.5),
            axes.c2p(4.75,-2.75),
        ]

        dots = []
        text_xi = []

        for i, p in enumerate(points_seq):

            new_dot = Dot(p, color=dark_blue, radius=0.08).shift(0.3*DR)
            dots.append(new_dot)

            if i % 2 == 0:
                label = MathTex(rf"y_{i+1}", color=BLACK).scale(0.7).next_to(new_dot, UP)
            else:
                label = MathTex(rf"y_{i+1}", color=BLACK).scale(0.7).next_to(new_dot, DOWN)

            text_xi.append(label)

        # -------------------- Arrow --------------------
        arrow = Arrow(
            start=dots[-1].get_center(),
            end=limit_dot.get_center(),
            color=BLACK,
            stroke_width=4,
            tip_length=0.15,
            tip_shape=StealthTip,
        )

        # -------------------- Shape Y --------------------
        smooth_shape_copy = smooth_shape.copy()
        smooth_shape_copy.set_color(dark_orange)
        smooth_shape_copy.scale(0.85)
        smooth_shape_copy.shift(0.45*UL)

        text_y = Text("Y", color=BLACK).next_to(smooth_shape_copy, RIGHT)

        # -------------------- Group Everything --------------------
        all_objects = VGroup(
            # grid,
            # axes,
            smooth_shape,
            text_x,
            limit_dot,
            limit_text,
            *dots,
            *text_xi,
            arrow,
            # smooth_shape_copy,
            # text_y,
        )

        all_objects.scale(1.1).move_to(ORIGIN).shift(1.5*RIGHT)
        # self.play(
        #     Create(grid),
        # )
        self.play(
            FadeIn(all_objects),
        )
        self.wait(1)

        # self.play(
        #     FadeOut(
        #         VGroup(*[
        #             arrow, limit_text,
        #         ])
        #     )
        # )
        limit_dot_modify = Dot(
            axes.c2p(5.5, -3.5),
            stroke_color=dark_pink, stroke_width=2, fill_color=WHITE, fill_opacity=1,
            radius=0.12
        ).move_to(limit_dot.get_center())
        self.play(
            FadeTransform(limit_dot, limit_dot_modify),
        )

        self.wait(0.5)
        self.play(
            FadeOut(
                VGroup(*[
                    arrow, limit_text, *dots, *text_xi,
                ])
            )
        )
        limit_points_seq = [
            Dot(axes.c2p(-2,4), stroke_color=dark_pink, stroke_width=2, fill_color=WHITE, fill_opacity=1, radius=0.12).shift(0.3*DR + 1.5*RIGHT),
            Dot(axes.c2p(1,2), stroke_color=dark_pink, stroke_width=2, fill_color=WHITE, fill_opacity=1, radius=0.12).shift(0.3*DR + 1.5*RIGHT),
            Dot(axes.c2p(-3,-3), stroke_color=dark_pink, stroke_width=2, fill_color=WHITE, fill_opacity=1, radius=0.12).shift(1.5*RIGHT),
        ]
        self.play(
            FadeIn(
                VGroup(*limit_points_seq)
            ),
        )
        self.wait(1)
        text_incomplete_part1 = MathTex(r"\text{Incomplete}",color=BLACK).scale(1.5)
        text_incomplete_part2 = MathTex(r"\text{  Space  }",color=BLACK).scale(1.5)
        text_incomplete = VGroup(text_incomplete_part1, text_incomplete_part2).arrange(DOWN).to_corner(UL)
        self.play(
            Write(text_incomplete),
        )
        self.wait(1)
        
        limit_points_seq_2 = [
            Dot(axes.c2p(-2,4), stroke_color=dark_pink, stroke_width=2, fill_color=dark_pink, fill_opacity=1, radius=0.12).shift(0.3*DR + 1.5*RIGHT),
            Dot(axes.c2p(1,2), stroke_color=dark_pink, stroke_width=2, fill_color=dark_pink, fill_opacity=1, radius=0.12).shift(0.3*DR + 1.5*RIGHT),
            Dot(axes.c2p(-3,-3), stroke_color=dark_pink, stroke_width=2, fill_color=dark_pink, fill_opacity=1, radius=0.12).shift(1.5*RIGHT),
            Dot(limit_dot.get_center(), stroke_color=dark_pink, stroke_width=2, fill_color=dark_pink, fill_opacity=1, radius=0.12),
        ]
        self.play(
            FadeTransform(
                VGroup(*[limit_points_seq, limit_dot_modify]),
                VGroup(*limit_points_seq_2),
            ),
        )
        self.wait(1)
        text_complete_part1 = MathTex(r"\text{Complete}",color=BLACK).scale(1.5)
        text_complete_part2 = MathTex(r"\text{  Space  }",color=BLACK).scale(1.5)
        text_complete = VGroup(text_complete_part1, text_complete_part2).arrange(DOWN).to_corner(UL)
        self.play(
            Transform(text_incomplete, text_complete),
        )
        self.wait(1)

        fade_out_list = [
            smooth_shape,
            text_x,
            limit_points_seq_2,
            text_incomplete,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list))
        )
        self.wait(1)


    def scene5_subScene0(self, title):
        """ constructing metrics with norms """
        # metric induced by the norm

        text_metric_space = MathTex(r"\text{Metric space}",color=dark_green).move_to(title.get_center()+DOWN).scale(2)
        text_metric_space_parts = MathTex(r"(",r"X",r",",r"d",r")",color=dark_blue,arg_separator="  ").move_to(text_metric_space.get_center()+1.6*DOWN).scale(2)
        # rect_x = SurroundingRectangle(
        #     text_metric_space_parts[1],
        #     color=dark_pink,        
        #     buff=0.1,          
        #     fill_opacity=0,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )
        # text_vector_space = MathTex(r"\text{Vector space}",color=dark_pink).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*LEFT).scale(2)
        # rect_vec_x = SurroundingRectangle(
        #     text_vector_space,
        #     color=dark_pink,        
        #     buff=0.1,          
        #     fill_opacity=0,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )
        # arrow_x = CurvedArrow(
        #     start_point=text_metric_space_parts[1].get_left()+0.1*LEFT,
        #     end_point=rect_vec_x.get_top()+0.2*UP,
        #     angle=PI/2,
        #     stroke_width=6,
        #     color=dark_pink,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # rect_d = SurroundingRectangle(
        #     text_metric_space_parts[3],
        #     color=dark_orange,        
        #     buff=0.2,          
        #     fill_opacity=0,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )
        # text_distance = MathTex(r"\text{Metric}",color=dark_orange).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        # rect_distance = SurroundingRectangle(
        #     text_distance,
        #     color=dark_orange,        
        #     buff=0.2,          
        #     fill_opacity=0,    
        #     stroke_width=3,    
        #     corner_radius=0.15 
        # )
        # arrow_d = CurvedArrow(
        #     start_point=text_metric_space_parts[3].get_right()+0.2*RIGHT,
        #     end_point=rect_distance.get_top()+0.2*UP,
        #     angle=-PI/2,
        #     stroke_width=6,
        #     color=dark_orange,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Write(text_metric_space),
        # )
        # self.wait(1)
        # self.play(
        #     Write(text_metric_space_parts[::2]),
        # )
        # self.wait(1)
        # self.play(
        #     Write(text_metric_space_parts[1]),
        #     Create(rect_x),
        #     Create(arrow_x),
        #     Create(rect_vec_x),
        #     Write(text_vector_space),
        # )
        # self.wait(1)
        # self.play(
        #     Write(text_metric_space_parts[3]),
        #     Create(rect_d),
        #     Create(arrow_d),
        #     Create(rect_distance),
        #     Write(text_distance),
        # )
        # self.wait(1)

        # fade_out_list = [text_metric_space, text_metric_space_parts, rect_x, 
        #                  arrow_x, rect_vec_x, text_vector_space,
        #                  rect_d, arrow_d, rect_distance, text_distance]
        # self.play(
        #     FadeOut(VGroup(*fade_out_list)),
        # )

        # self.wait(1)

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-6, 7, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=13,
        ).move_to([0, 0, 0]+DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-6, 7, 1],
            y_length=8,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)
        self.play(
            Create(plane),
            Create(axes)
        )
        self.wait(1.5)

        # dot at tip of vector
        tip_x = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        tip_x_text = MathTex("A = (x_1,y_1)",color=BLACK).next_to(tip_x,UP).shift(0.6*RIGHT)
        self.play(
            FadeIn(tip_x),
            Write(tip_x_text),
        )
        self.wait(0.5)

        tip_y = Dot(axes.c2p(2,6), color=dark_green, radius=0.07)
        tip_y_text = MathTex("B = (x_2,y_2)",color=BLACK).next_to(tip_y,UP)  #.shift(0.1*RIGHT)
        self.play(
            FadeIn(tip_y),
            Write(tip_y_text),
        )
        self.wait(2)

        dot_line_distance =  DashedLine(
            start=axes.c2p(6,4),
            end=axes.c2p(2,6), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_orange,
        )
        text_distance = MathTex(r"\text{Distance}",color=dark_orange).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        text_distance.scale(0.5).next_to(dot_line_distance,DOWN) #.shift(0.4*RIGHT)
        text_dxy = MathTex(r"d(A,B)",color=dark_orange).shift(axes.c2p(0,0)+DOWN+1.5*LEFT).scale(1.5)

        self.play(
            Create(dot_line_distance),
            Write(text_distance),
        )
        self.play(
            Write(text_dxy),
        )
        self.wait(2)
        self.play(
            FadeOut(text_distance),
        )

        vector_amb = Arrow(
            start=axes.c2p(2,6),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        text_vec_amb = MathTex(r"\vec{BA}",color=dark_orange).move_to(vector_amb.get_center()+0.5*UP)
        text_norm_ab = MathTex(r" = ",r"\|\vec{BA}\|",color=dark_orange).scale(1.5).next_to(text_dxy,RIGHT)

        self.play(
            Transform(dot_line_distance, vector_amb),
        )
        self.wait(1.5)
        self.play(
            Write(text_vec_amb),
            Write(text_norm_ab),
        )
        self.wait(2)

        vector_a = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        vector_b = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(2,6),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_vec_b = MathTex(r"\vec{b}",color=dark_green).move_to(vector_b.get_center()+0.5*LEFT)
        text_vec_a = MathTex(r"\vec{a}",color=dark_red).move_to(vector_a.get_center()+0.5*RIGHT)

        self.play(
            GrowArrow(vector_a, run_time=1.2, rate_func=rush_from),
            Write(text_vec_a),
        )
        self.wait(1.5)
        self.play(
            GrowArrow(vector_b, run_time=1.2, rate_func=rush_from),
            Write(text_vec_b),
        )
        self.wait(1.5)

        text_vec_amb_2 = MathTex(r"\vec{BA} = ",r"\vec{a} - \vec{b}",color=dark_pink).move_to(vector_amb.get_center()+0.5*UP+7*LEFT).scale(2)
        text_norm_ab_2 = MathTex(r" = ",r"\|\vec{a} - \vec{b}\|",color=dark_orange).next_to(text_norm_ab,DOWN).scale(1.5)

        self.play(
            TransformFromCopy(text_vec_amb, text_vec_amb_2),
        )
        self.wait(1.5)
        self.play(
            TransformFromCopy(VGroup(text_vec_amb_2,text_norm_ab), text_norm_ab_2),
        )
        self.wait(1.5)

        fade_out_list = [
            plane, axes, tip_x , tip_x_text , tip_y , tip_y_text , text_dxy , dot_line_distance,
            text_vec_amb , text_norm_ab , vector_a , vector_b, text_vec_a , text_vec_b, 
            text_vec_amb_2, text_norm_ab_2, 
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

        self.wait(1)

    def scene5_subScene1(self, title, prove_1, distance):
        """prove d is a meter part 1"""

        # proof
        step_1 = MathTex(r"d(x,y) = 0",color=BLACK).scale(1.5).move_to(prove_1.get_center()+2*DOWN)
        step_2 = MathTex(r"\iff",r"\|x-y\| = 0",color=BLACK).scale(1.5).next_to(step_1,RIGHT)
        step_3 = MathTex(r"\iff",r"x-y = 0",color=BLACK).scale(1.5).next_to(step_2,DOWN).shift(0.3*LEFT)
        step_2to3 = MathTex(r"(N1)",color=dark_orange).scale(1.5).next_to(step_3,RIGHT)
        step_4 = MathTex(r"\iff",r"x = y \quad . \blacksquare",color=BLACK).scale(1.5).next_to(step_3,DOWN) #.shift(0.5*LEFT)
        square_for_end_proof = Square(0.3,color=BLACK).scale(1.5).next_to(step_4,RIGHT)
        prove_1_group = VGroup(step_1, step_2, step_3, step_2to3, step_4).shift(3*LEFT+0.7*UP)
        rect_prove_1 = SurroundingRectangle(
            prove_1_group,
            color=dark_orange,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            Write(prove_1),
        )
        self.wait(2)

        self.play(
            Create(rect_prove_1),
        )
        self.wait(1)
        self.play(
            TransformFromCopy(prove_1[1], step_1),
        )
        self.wait(1.3)
        self.play(
            TransformFromCopy(distance[2],step_2),
        )
        self.wait(1.3)
        self.play(
            Write(step_2to3),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(VGroup(step_2to3,step_2),step_3),
        )
        self.wait(1.3)
        self.play(
            Write(step_4),
        )
        self.wait(1.3)
        # self.play(
        #     Create(square_for_end_proof),
        # )
        # self.wait(0.3)

        # shape

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-2, 5, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=4,
            x_length=13,
        ).move_to([0, 0, 0]+1.5*DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-2, 5, 1],
            y_length=4,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+1.5*DOWN)

        self.play(
            FadeTransform(VGroup(prove_1_group,rect_prove_1),VGroup(plane,axes)),
        )
        self.wait(1)

        tip_x = Dot(axes.c2p(6,4), color=dark_orange, radius=0.09)
        tipx_text = MathTex("x",color=BLACK).next_to(tip_x,DOWN)
        self.play(
            FadeIn(tip_x),
            Write(tipx_text),
        )

        tip_y = Dot(axes.c2p(2,1), color=dark_purple, radius=0.09)
        tipy_text = MathTex("y",color=BLACK).next_to(tip_y,UP)
        self.play(
            FadeIn(tip_y),
            Write(tipy_text),
        )
        self.wait(1)

        dot_line_distance =  Arrow(
            start=axes.c2p(2,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            GrowArrow(dot_line_distance),
        )
        self.wait(2)

        dot_line_distance_new = Line(
            start=axes.c2p(2,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_red,
        )
        self.play(
            Transform(dot_line_distance, dot_line_distance_new),
            run_time=0.1
        )
        self.play(
            dot_line_distance.animate.scale(
                0,
                about_point=dot_line_distance.get_start()  
            ),
            FadeOut(tip_y),
            VGroup(tip_x,tipx_text).animate.move_to(axes.c2p(2,1)),
            rum_time=2
        )

        self.wait(1)

        fade_out_list = [
            plane, axes, tip_x , tipx_text, tipy_text
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )
        self.wait(1)

    def scene5_subScene2(self, title, prove_1, prove_2, distance):
        """prove d is a meter part 2"""

        # proof
        step_1 = MathTex(r"d(x,y)",color=BLACK).scale(1.5).move_to(prove_2.get_center()+2*DOWN)
        step_2 = MathTex(r" = ",r"\|x-y\|",color=BLACK).scale(1.5).next_to(step_1,RIGHT)
        step_3 = MathTex(r" = ",r"\|(-1) \, (y-x)\|",color=BLACK).scale(1.5).next_to(step_2,RIGHT)
        step_4 = MathTex(r" = ",r"|-1| \, \|(y-x)\|",color=BLACK).scale(1.5).next_to(step_2,DOWN).shift(1.3*RIGHT)
        step_3to4 = MathTex(r"(N2)",color=dark_orange).scale(1.5).next_to(step_4,RIGHT)
        step_5 = MathTex(r" = ",r"\|y-x\|",color=BLACK).scale(1.5).next_to(step_4,DOWN).shift(1.1*LEFT)
        step_6 = MathTex(r" = ",r"d(y,x) \quad . \blacksquare",color=BLACK).scale(1.5).next_to(step_5,RIGHT)
        square_for_end_proof = Square(0.3,color=BLACK).scale(1.5).next_to(step_6,RIGHT)
        prove_2_group = VGroup(step_1, step_2, step_3, step_4, step_3to4, step_5, step_6).shift(4*LEFT+0.7*UP)
        rect_prove_2 = SurroundingRectangle(
            prove_2_group,
            color=dark_orange,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            TransformMatchingTex(prove_1, prove_2),
        )
        self.wait(1.3)

        self.play(
            Create(rect_prove_2),
        )
        self.wait(1.3)
        self.play(
            TransformFromCopy(prove_2[1], step_1),
        )
        self.wait(1.3)
        self.play(
            TransformFromCopy(distance[2],step_2),
        )
        self.wait(1.3)
        self.play(
            Write(step_3),
        )
        self.wait(1.3)
        self.play(
            Write(step_3to4),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(VGroup(step_3to4,step_3),step_4),
        )
        self.wait(1.3)
        self.play(
            Write(step_5),
        )
        self.wait(1.3)
        self.play(
            Write(step_6),
        )
        self.wait(1.3)
        # self.play(
        #     Create(square_for_end_proof),
        # )
        # self.wait(0.3)

        # step_1.set_color(dark_red)
        # step_6.set_color(dark_red)

        self.wait(1.3)

        # shape

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-2, 5, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=4,
            x_length=13,
        ).move_to([0, 0, 0]+1.5*DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-2, 5, 1],
            y_length=4,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+1.5*DOWN)

        self.play(
            FadeTransform(VGroup(prove_2_group,rect_prove_2),VGroup(plane,axes)),
        )
        self.wait(1.5)

        tip_x = Dot(axes.c2p(6,4), color=dark_orange, radius=0.09)
        tipx_text = MathTex("x",color=BLACK).next_to(tip_x,DOWN)
        self.play(
            FadeIn(tip_x),
            Write(tipx_text),
        )

        tip_y = Dot(axes.c2p(2,1), color=dark_purple, radius=0.09)
        tipy_text = MathTex("y",color=BLACK).next_to(tip_y,UP)
        self.play(
            FadeIn(tip_y),
            Write(tipy_text),
        )
        self.wait(0.5)

        vector_1 = Arrow(
            start=axes.c2p(2,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        vector_2 = Arrow(
            start=axes.c2p(6,4),
            end=axes.c2p(2,1),
            buff=0,
            stroke_width=6,
            color=dark_terquise,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        prove_2.set_color_by_tex(r"d(x,y)",dark_green)
        self.play(
            GrowArrow(vector_1),
        )
        self.wait(2)

        self.play(
            vector_1.animate.shift(8*LEFT),
            run_time=1
        )
        self.wait(1)

        prove_2.set_color_by_tex(r"d(x,y)",BLACK)
        prove_2.set_color_by_tex(r"d(y,x)",dark_terquise)
        self.play(
            GrowArrow(vector_2),
        )
        self.wait(2)

        self.play(
            vector_2.animate.shift(7.7*LEFT+0.4*DOWN),
            run_time=1
        )
        self.wait(1)
        prove_2.set_color_by_tex(r"d(y,x)",BLACK)

        comp_line = Line(vector_1.get_start(),vector_1.get_end(),color=dark_red, stroke_width=10)
        self.play(
            Create(comp_line),
        )
        self.wait(0.3)
        self.play(
            comp_line.animate.move_to(vector_2.get_center()),
            run_time=1
        )
        self.wait(2)

        fade_out_list = [
            plane, axes, tip_x ,tip_y , tipx_text, tipy_text, vector_1, vector_2, comp_line
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )
        self.wait(2)

    def scene5_subScene3(self, title, prove_2, prove_3, distance):
        """prove d is a meter part 3"""
        # proof
        step_1 = MathTex(r"d(x,y)",color=BLACK).scale(1.5).move_to(prove_2.get_center()+2*DOWN)
        step_2 = MathTex(r" = ",r"\|x-y\|",color=BLACK).scale(1.5).next_to(step_1,RIGHT)
        step_3 = MathTex(r" = ",r"\|",r"x ",r" - z",r" + ",r"z",r"- y",r"\|",color=BLACK).scale(1.5).next_to(step_2,DOWN).shift(1.3*RIGHT)
        step_3.set_color_by_tex(r" - z",dark_blue)
        step_3.set_color_by_tex(r"z",dark_blue)
        step_3.set_color_by_tex(r" + ",dark_blue)
        rect_step_3_x = SurroundingRectangle(
            step_3[2:4],
            color=dark_pink,        
            buff=0.15,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        rect_step_3_y = SurroundingRectangle(
            step_3[5:7],
            color=dark_purple,        
            buff=0.15,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        step_4 = MathTex(r" \le ",r"\|x-z\|",r" + ",r"\|z-y\|",color=BLACK).scale(1.5).next_to(step_3,DOWN).shift(0.2*RIGHT)
        step_4.set_color_by_tex(r"\|x-z\|",dark_pink)
        step_4.set_color_by_tex(r"\|z-y\|",dark_purple)
        step_3to4 = MathTex(r"(N3)",color=dark_orange).scale(1.5).next_to(step_4,RIGHT)
        step_5 = MathTex(r" = ",r"d(x,z) + d(z,y) \quad . \blacksquare",color=BLACK).scale(1.5).next_to(step_4,DOWN).shift(0.5*LEFT)
        square_for_end_proof = Square(0.3,color=BLACK).scale(1.5).next_to(step_5,RIGHT)
        prove_2_group = VGroup(step_1, step_2, step_3, rect_step_3_x, rect_step_3_y, step_4, step_3to4, step_5).shift(4*LEFT+0.7*UP)
        rect_prove_2 = SurroundingRectangle(
            prove_2_group,
            color=dark_orange,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        self.play(
            TransformMatchingTex(prove_2, prove_3),
        )
        self.wait(2)

        self.play(
            Create(rect_prove_2),
        )
        self.wait(1.3)
        self.play(
            TransformFromCopy(prove_2[1], step_1),
        )
        self.wait(1.3)
        self.play(
            TransformFromCopy(distance[2],step_2),
        )
        self.wait(1.3)
        self.play(
            Write(step_3),
        )
        self.wait(1.3)
        self.play(
            Create(rect_step_3_x),
        )
        self.wait(0.5)
        self.play(
            Create(rect_step_3_y),
        )
        self.wait(0.5)
        self.play(
            Write(step_3to4),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(VGroup(step_3to4,step_3),step_4),
        )
        self.wait(1.3)
        self.play(
            Write(step_5),
        )
        self.wait(1.3)
        # self.play(
        #     Create(square_for_end_proof),
        # )
        # self.wait(0.3)

        # step_1.set_color(dark_red)
        # step_5.set_color(dark_red)
        # step_5.set_color_by_tex(r" = ",BLACK)
        # step_4.set_color_by_tex(r" \le ",dark_red)

        self.wait(1.3)

        # shape

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-2, 5, 1],
            x_range=[-8, 8, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=4,
            x_length=13,
        ).move_to([0, 0, 0]+1.5*DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-2, 5, 1],
            y_length=4,
            x_range=[-8, 8, 1],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+1.5*DOWN)

        self.play(
            FadeTransform(VGroup(prove_2_group,rect_prove_2),VGroup(plane,axes)),
        )

        tip_x = Dot(axes.c2p(6,4), color=dark_orange, radius=0.09)
        tipx_text = MathTex("x",color=BLACK).next_to(tip_x,UP)
        self.play(
            FadeIn(tip_x),
            Write(tipx_text),
        )

        tip_y = Dot(axes.c2p(2,1), color=dark_purple, radius=0.09)
        tipy_text = MathTex("y",color=BLACK).next_to(tip_y,UP)
        self.play(
            FadeIn(tip_y),
            Write(tipy_text),
        )
        self.wait(2)

        vector_1 = Arrow(
            start=axes.c2p(2,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        prove_3.set_color_by_tex(r"d(x,y)",dark_green)
        self.play(
            GrowArrow(vector_1),
        )
        self.wait(0.5)

        tip_z = Dot(axes.c2p(5,1), color=dark_blue, radius=0.09)
        tipz_text = MathTex("z",color=BLACK).next_to(tip_z,DOWN)
        self.play(
            FadeIn(tip_z),
            Write(tipz_text),
        )
        self.wait(0.5)

        vector_2 = Arrow(
            start=axes.c2p(5,1),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        vector_3 = Arrow(
            start=axes.c2p(2,1),
            end=axes.c2p(5,1),
            buff=0,
            stroke_width=6,
            color=dark_purple,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        prove_3.set_color_by_tex(r"d(x,z)",dark_pink)
        self.play(
            GrowArrow(vector_2),
        )
        self.wait(0.5)

        prove_3.set_color_by_tex(r"d(z,y)",dark_purple)
        self.play(
            GrowArrow(vector_3),
        )
        self.wait(2)
        prove_3.set_color_by_tex(r"d(x,y)",BLACK)
        prove_3.set_color_by_tex(r"d(x,z)",BLACK)
        prove_3.set_color_by_tex(r"d(z,y)",BLACK)

        fade_out_list = [
            plane, axes, tip_x ,tip_y , tipx_text, tipy_text, vector_1, vector_2, vector_3, tip_z, tipz_text
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )
        self.wait(1)

    def scene5_subScene4(self, title):
        """definition of Metric space"""

        text_normed_space_ = MathTex(r"\text{Normed space}",color=dark_green).move_to(title.get_center()+DOWN).scale(2)
        text_normed_space_parts_ = MathTex(r"( \, ",r"X",r" \, , \, ",r"\|.\|",r" \, )",color=dark_blue,arg_separator="  ").move_to(text_normed_space_.get_center()+1.6*DOWN).scale(2)
        rect_x_ = SurroundingRectangle(
            text_normed_space_parts_[1],
            color=dark_pink,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_vector_space_ = MathTex(r"\text{Vector space}",color=dark_pink).move_to(text_normed_space_parts_.get_center()+2.6*DOWN+3*LEFT).scale(2)
        rect_vec_x_ = SurroundingRectangle(
            text_vector_space_,
            color=dark_pink,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_x_ = CurvedArrow(
            start_point=text_normed_space_parts_[1].get_left()+0.2*LEFT,
            end_point=rect_vec_x_.get_top()+0.2*UP,
            angle=PI/2,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        rect_d_ = SurroundingRectangle(
            text_normed_space_parts_[3],
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_distance_ = MathTex(r"\text{Norm}",color=dark_orange).move_to(text_normed_space_parts_.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        rect_distance_ = SurroundingRectangle(
            text_distance_,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_d_ = CurvedArrow(
            start_point=text_normed_space_parts_[3].get_right()+0.2*RIGHT,
            end_point=rect_distance_.get_top()+0.2*UP,
            angle=-PI/2,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        recall_norm_space_all_shapes = VGroup(*[
            text_normed_space_,
            text_normed_space_parts_,
            rect_x_,
            text_vector_space_,
            rect_vec_x_,
            arrow_x_,
            rect_d_,
            text_distance_,
            rect_distance_,
            arrow_d_,
        ])

        self.play(
            FadeIn(recall_norm_space_all_shapes),
        )

        text_metric_space = MathTex(r"\text{Metric space}",color=dark_green).move_to(title.get_center()+DOWN).scale(2)
        text_metric_space_parts = MathTex(r"( \, ",r"X",r" \, , \, ",r"d(x,y) = \|x - y\|",r" \, )",color=dark_blue,arg_separator="  ").move_to(text_metric_space.get_center()+1.6*DOWN).scale(2)
        rect_x = SurroundingRectangle(
            text_metric_space_parts[1],
            color=dark_pink,        
            buff=0.1,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_vector_space = MathTex(r"\text{Vector space}",color=dark_pink).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*LEFT).scale(2)
        rect_vec_x = SurroundingRectangle(
            text_vector_space,
            color=dark_pink,        
            buff=0.1,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_x = CurvedArrow(
            start_point=text_metric_space_parts[1].get_bottom()+0.1*LEFT+0.1*DOWN,
            end_point=rect_vec_x.get_top()+0.1*UP,
            angle=0,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        rect_d = SurroundingRectangle(
            text_metric_space_parts[3],
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_distance = MathTex(r"\text{Metric}",color=dark_orange).move_to(text_metric_space_parts.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        rect_distance = SurroundingRectangle(
            text_distance,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_d = CurvedArrow(
            start_point=text_metric_space_parts[3].get_bottom()+1*RIGHT+0.2*DOWN,
            end_point=rect_distance.get_top()+0.1*UP,
            angle=0,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        recall_norm_space_all_shapes = VGroup(*[

            VGroup(*[
                text_normed_space_parts_,
                rect_x_,
                arrow_x_,
                text_vector_space_,
                rect_vec_x_,
                rect_d_,
                arrow_d_,
                rect_distance_,
            ]),

            text_distance_,

            text_normed_space_,
        ])

        recall_metric_space_all_shapes = VGroup(*[

            VGroup(*[
                text_metric_space_parts,
                rect_x,
                arrow_x,
                text_vector_space,
                rect_vec_x,
                rect_d,
                arrow_d,
                rect_distance,
            ]),

            text_distance,
            
            text_metric_space,
        ])

        self.play(
            # FadeTransformPieces(recall_norm_space_all_shapes, recall_metric_space_all_shapes),
            # run_time=2
            LaggedStart(
                *[ Transform(recall_norm_space_all_shapes[i], recall_metric_space_all_shapes[i]) for i in range(3) ],
                lag_ratio=1.5,
            ),
            # run_time=2
        )

        # self.play(
        #     FadeIn(text_metric_space_parts),
        # )
        # self.wait(1)
        # self.play(
        #     # Write(text_metric_space_parts[1]),
        #     Create(rect_x),
        #     Create(arrow_x),
        #     Create(rect_vec_x),
        #     Write(text_vector_space),
        # )
        # self.wait(1)
        # self.play(
        #     # Write(text_metric_space_parts[3]),
        #     Create(rect_d),
        #     Create(arrow_d),
        #     Create(rect_distance),
        #     Write(text_distance),
        # )
        # self.wait(1)
        # self.play(
        #     Write(text_metric_space),
        # )
        self.wait(1)

        # fade_out_list = [text_metric_space ,text_metric_space_parts, rect_x, 
        #                  arrow_x, rect_vec_x, text_vector_space,
        #                  rect_d, arrow_d, rect_distance, text_distance]
        # self.play(
        #     FadeOut(VGroup(*fade_out_list)),
        # )

        self.play(
            FadeOut(recall_norm_space_all_shapes),
        )

        self.wait(1)

        # counterexample
        text_counterexample = MathTex(
            r"\text{Normed Space}",
            r"\xrightarrow{}",
            r"\text{Metric Space}",
            color=BLACK
        ).scale(1.2)

        not_reverse = MathTex(r"\not\leftarrow", color=BLACK).scale(1.2)

        # قرار دادن زیر فلش
        not_reverse.next_to(text_counterexample[1], DOWN, buff=0.05)

        group = VGroup(text_counterexample, not_reverse).to_edge(UP)

        rect_not_reverse = SurroundingRectangle(
            not_reverse,
            color=dark_purple,
            buff=0.08,
            stroke_width=3,
            corner_radius=0.15
        )

        counter_example1 = MathTex(r"d(x,y)=\sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\xi_j-\eta_j|}{1+|\xi_j-\eta_j|}", color=BLACK).next_to(group,DOWN,buff=2)
        counter_example2 = MathTex(r"\|x\| = ",r"d(x,0)=\sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\xi_j-0|}{1+|\xi_j-0|}", color=BLACK).next_to(counter_example1,DOWN,buff=0.5)
        counter_example3 = MathTex(r"\|x\| = ",r"d(x,0)=\sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\xi_j|}{1+|\xi_j|}", color=BLACK).move_to(counter_example2.get_center())
        counter_example_1and2 = VGroup(*[
            counter_example1,
            counter_example2
        ])
        title_text = Text("Counterexample", color= dark_purple, font_size=36)
        group_counter1 = VGroup(title_text, counter_example_1and2).arrange(DOWN, buff=0.3)

        rect_counter_example_part1 = RoundedRectangle(
            corner_radius=0.3,
            color= dark_purple,
            fill_color=light_purple,
            fill_opacity=0.2,
            width=group_counter1.width + 1,
            height=group_counter1.height + 0.8
        ).move_to(group_counter1.get_center())

        VGroup(*[group_counter1, rect_counter_example_part1]).shift(0.5*DOWN)

        # example_group_part1 = MathTex(
        #     r"\|\alpha x\|",
        #     color=BLACK,
        # )
        example_group_part2 = MathTex(
            r"\|\alpha x\|",
            r"= \sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\alpha\xi_j|}{1+|\alpha\xi_j|}",
            r"= \sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\alpha|\,|\xi_j|}{1+|\alpha|\,|\xi_j|}",
            color=BLACK,
        )
        # example_group_part3 = MathTex(
        #     r"= \sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\alpha|\,|\xi_j|}{1+|\alpha|\,|\xi_j|}",
        #     color=BLACK,
        # )
        example_group_part4 = MathTex(
            r"\ne",
            color=dark_red,
        )
        example_group_part5 = MathTex(
            r"\sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\alpha|\,|\xi_j|}{1+|\xi_j|}",
            r"= |\alpha|\sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\xi_j|}{1+|\xi_j|}",
            r"= |\alpha|\,\|x\|.",
            color=BLACK,
        )
        # example_group_part6 = MathTex(
        #     r"= |\alpha|\sum_{j=1}^{\infty}\frac{1}{2^j}\frac{|\xi_j|}{1+|\xi_j|}",
        #     color=BLACK,
        # )
        # example_group_part7 = MathTex(
        #     r"= |\alpha|\,\|x\|.",
        #     color=BLACK,
        # )

        example_group = VGroup(*[
            title_text,
            # example_group_part1,
            example_group_part2,
            # example_group_part3,
            example_group_part4,
            example_group_part5,
            # example_group_part6,
            # example_group_part7,
        ]).arrange(DOWN,buff=0.3)

        rect_counter_example_part2 = RoundedRectangle(
            corner_radius=0.3,
            color= dark_purple,
            fill_color=light_purple,
            fill_opacity=0.2,
            width=example_group.width + 1,
            height=example_group.height + 0.8
        ).move_to(example_group.get_center())

        VGroup(example_group, rect_counter_example_part2).shift(0.5*DOWN)

        rect_not_reverse = SurroundingRectangle(
            not_reverse,
            color=dark_purple,
            buff=0.08,
            stroke_width=3,
            corner_radius=0.15
        )

        self.play(
            Write(text_counterexample),
        )
        self.play(
            Write(not_reverse),
        )
        self.wait(0.5)
        self.play(
            Create(rect_not_reverse),
        )
        self.play(
            Create(rect_counter_example_part1),
            Write(title_text),
            Write(counter_example1),
        )
        self.wait(0.5)
        self.play(
            Write(counter_example2),
        )
        self.wait(0.5)
        counter_example3.move_to(counter_example2.get_center())
        self.play(
            TransformMatchingTex(counter_example2, counter_example3),
        )
        self.wait(0.5)
        self.play(
            TransformMatchingShapes(
                VGroup(*[rect_counter_example_part1, counter_example1, counter_example3]),
                VGroup(*[rect_counter_example_part2, example_group]),
            )
        )
        self.wait(1)
        fade_out_list2 = VGroup(*[
            text_counterexample,
            rect_not_reverse,
            not_reverse,
            rect_counter_example_part2, 
            example_group,
        ])
        self.play(
            FadeOut(fade_out_list2),
        )
        self.wait(0.5)


        self.wait(1)

        circle_metric = Circle(4,dark_pink,fill_color=dark_pink,fill_opacity=0.1)
        text_metric_space = MathTex(r"\text{Metric space}",color=dark_pink).scale(2).move_to(circle_metric.get_center()+2.3*UP)

        circle_norm = Circle(2.8,dark_purple,fill_color=dark_purple,fill_opacity=0.1).shift(1*DOWN)
        text_norm_space = MathTex(r"\text{Normed space}",color=dark_purple).scale(1.5).move_to(circle_norm.get_center()+1.3*UP)

        self.play(
            Write(text_norm_space),
            Create(circle_norm),
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(VGroup(text_norm_space, circle_norm), VGroup(text_metric_space, circle_metric)),
        )

        self.wait(1)

        fade_out_list = [
            circle_metric,
            text_metric_space,
            text_norm_space,
            circle_norm,
        ]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

        self.wait(1)

    def scene5(self,title):
        # self.play(
        #     Write(title),
        # )
        # self.wait(1)
        # self.play(
        #     FadeOut(title),
        # )
        # self.wait(0.5)

        # constructing metrics with norms
        # self.scene5_subScene0(title)

        # proof needed things
        distance = MathTex(r"d(x,y) ",r" = ",r"\|x-y\|",color=BLACK).scale(2).move_to(title.get_center()+0.2*DOWN)
        rect_distance = SurroundingRectangle(
            distance,
            color=dark_blue,        
            buff=0.3,          
            fill_opacity=0.1,    
            stroke_width=5,    
            corner_radius=0.15 
        )

        # self.play(
        #     Create(rect_distance),
        #     Write(distance),
        # )
        # self.wait(1)

        text_claim1 = MathTex(r"\text{Claim : }",color=BLACK).scale(1.1)
        text_claim2 = MathTex(r"d \text{ is a } " ,r"\text{metric}",color=BLACK).scale(1.1)
        text_claim2.set_color_by_tex(r"\text{metric}",color=dark_blue)
        text_claim = VGroup(text_claim1, text_claim2).arrange(DOWN,buff=0.3)

        # self.play(
        #     VGroup(distance,rect_distance).scale(1).animate.to_edge(UL),
        #     Write(text_claim.move_to(rect_distance.get_right()+0.5*RIGHT+0.2*DOWN)),
        # )
        # self.wait(2)

        # prove part 1
        prove_1 = MathTex(r"\quad",r"d(x,y) = 0",r"\iff",r"x = y",color=BLACK).scale(1.5).move_to(title.get_center()+2*DOWN)
        # proof_1_needed = [
        #     prove_1, distance
        # ]
        # self.scene5_subScene1(title, *proof_1_needed)

        # prove part 2
        prove_2 = MathTex(r"\quad",r"d(x,y)",r" = ",r"d(y,x)",color=BLACK).scale(1.5).move_to(title.get_center()+2*DOWN)
        # proof_2_needed = [
        #     prove_1, prove_2, distance
        # ]
        VGroup(distance,rect_distance).scale(1).to_edge(UL)
        text_claim.move_to(rect_distance.get_right()+3.5*RIGHT+0.2*DOWN)
        # self.add(prove_2, distance, rect_distance, text_claim)
        # self.scene5_subScene2(title,*proof_2_needed)

        # # prove part 3
        prove_3 = MathTex(r"\quad",r"d(x,y)",r" \le ",r"d(x,z)",r" + ",r"d(z,y)",color=BLACK).scale(1.5).move_to(title.get_center()+2*DOWN)
        proof_3_needed = [
            prove_2, prove_3, distance
        ]
        # self.scene5_subScene3(title, *proof_3_needed)

        # fade_out_list = [
        #     distance, rect_distance, text_claim, prove_3
        # ]
        # self.play(
        #     FadeOut(VGroup(*fade_out_list)),
        # )

        # normed space
        self.scene5_subScene4(title)

    def scene4_subScene0(self,title):
        # length

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-6, 7, 0.5],
            x_range=[-8, 8, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=8,
            x_length=13,
        ).move_to([0, 0, 0]+DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-6, 7, 0.5],
            y_length=8,
            x_range=[-8, 8, 0.5],
            x_length=13,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)
        # self.play(
        #     Create(plane),
        #     Create(axes),
        # )

        # # dot at tip of vector
        # tip = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        # tip_text = MathTex("(x,y)",color=BLACK).next_to(tip,UP)
        # self.play(
        #     FadeIn(tip),
        #     Write(tip_text),
        # )
        # self.wait(5)

        # norm2_2d = MathTex(
        #     r"\text{Vector length }",r" \text{is } ",r"\sqrt{x^2 + y^2}",color=BLACK
        # ).move_to(axes.get_center()+1*DOWN)
        # # draw vector in (0,0)
        # vector = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,4),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # self.play(
        #     Write(norm2_2d[0]),
        #     GrowArrow(vector, run_time=1.2, rate_func=rush_from),
        # )
        # self.wait(5)

        # for _ in range(2):
        #     self.play(
        #         tip.animate.scale(2).set_color(BLACK),
        #         rate_func=there_and_back,
        #     )

        # dot_line_1 =  DashedLine(
        #     start=axes.c2p(6,4),
        #     end=axes.c2p(6,0), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_red,
        # )

        # dot_line_1_result = Line(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,0), 
        #     color=dark_pink,
        # )

        # text_dot_x = MathTex(r"x",color=BLACK).move_to(dot_line_1_result.get_center()+0.3*UP)

        # dot_line_2 =  DashedLine(
        #     start=axes.c2p(6,4),
        #     end=axes.c2p(0,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_not_green,
        # )

        # dot_line_2_result = Line(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(0,4), 
        #     color=dark_purple,
        # )

        # text_dot_y = MathTex(r"y",color=BLACK).move_to(dot_line_2_result.get_center()+0.3*LEFT)

        # self.play(
        #     Create(dot_line_1),
        #     Create(dot_line_1_result),
        #     Write(text_dot_x),

        #     Create(dot_line_2),
        #     Create(dot_line_2_result),
        #     Write(text_dot_y),

        #     run_time=1
        # )
        # self.play(
        #     FadeOut(dot_line_1),
        #     FadeOut(dot_line_2),
        # )
        # dot_line_1_result_group_with_text_x = VGroup(dot_line_1_result,text_dot_x)
        # self.play(
        #     dot_line_1_result_group_with_text_x.animate.move_to(dot_line_2.get_center()+0.19*UP),
        #     run_time=0.5
        # )

        # triangle_Euclid = Polygon(
        #     tip.get_center(),
        #     axes.c2p(0,0),
        #     axes.c2p(0,4),
        # )
        # triangle_Euclid.set_stroke(color=dark_terquise, width=8)
        # triangle_Euclid.set_fill(dark_terquise, opacity=0.2)

        # self.play(
        #     DrawBorderThenFill(triangle_Euclid,1),
        # )
        # self.play(
        #     triangle_Euclid.animate.set_fill(WHITE),
        #     run_time=0.5
        # )

        # for _ in range(2):
        #     self.play(
        #         vector.animate.set_stroke(width=20).set_color("#9A0000"),
        #         rate_func=there_and_back,
        #     )
        # self.wait(1)
        # self.play(
        #     Write(norm2_2d[1]),
        #     Write(norm2_2d[2]),
        # )
        

        # # num example 
        # # text_num_x = MathTex(r"4",color=dark_pink).move_to(text_dot_x.get_center())
        # # text_num_y = MathTex(r"3",color=dark_pink).move_to(text_dot_y.get_center())
        # # text_length_vector_1 = MathTex(r"\sqrt{4^2 + 3^2}",color=dark_pink).move_to(vector.get_center()+1.2*RIGHT)
        # # text_length_vector_2part0 = MathTex(r"\sqrt{16 + 9}",color=dark_pink).move_to(vector.get_center()+1.2*RIGHT)
        # # text_length_vector_2part1 = MathTex(r"\sqrt{ 25 }",color=dark_pink).move_to(text_length_vector_2part0.get_center())
        # # text_length_vector_2part2 = MathTex(r"5",color=dark_pink).move_to(text_length_vector_2part1.get_center())
        # # self.play(
        # #     FadeOut(text_dot_x),
        # #     FadeIn(text_num_x)
        # # )
        # # self.wait(0.5)
        # # self.play(
        # #     FadeOut(text_dot_y),
        # #     FadeIn(text_num_y)
        # # )
        # # self.wait(0.5)
        # # self.play(
        # #     FadeIn(text_length_vector_1),
        # # )
        # # self.wait(1)
        # # self.play(
        # #     FadeTransform(text_length_vector_1,text_length_vector_2part0),
        # # )
        # # self.wait(0.7)
        # # self.play(
        # #     FadeTransform(text_length_vector_2part0,text_length_vector_2part1),
        # # )
        # # self.wait(0.7)
        # # self.play(
        # #     FadeTransform(text_length_vector_2part1,text_length_vector_2part2),
        # # )
        # # self.wait(1)
        # # self.play(
        # #     FadeOut(text_num_x),
        # #     FadeIn(text_dot_x),
        # #     FadeOut(text_num_y),
        # #     FadeIn(text_dot_y),
        # #     FadeOut(text_length_vector_2part2),
        # # )
        # # self.wait(1)

        # self.play(
        #     FadeOut(triangle_Euclid),
        #     FadeOut(dot_line_1_result_group_with_text_x),
        #     FadeOut(text_dot_y),
        #     FadeOut(dot_line_1_result),
        #     FadeOut(dot_line_2_result),
        # )
        # self.wait(3)


        # # properties of length
        # # 1
        # text_1 = MathTex(r"\text{Always non-negative}",color=dark_pink
        # ).scale(1.3).to_edge(LEFT).shift(0.5*RIGHT+UP)
        # text_1_part2 = MathTex(r"\ge 0",color=dark_pink
        # ).scale(1.3).next_to(norm2_2d,RIGHT)
        # self.play(
        #     Write(text_1),
        #     Write(text_1_part2),
        # )
        # self.wait(1.5)
        # self.play(
        #     FadeOut(text_1_part2),
        # )

        # # 2
        # text_2_part1 = MathTex(r"\text{Vector is }",r"\vec{0}",color=dark_pink
        # ).scale(1.3)
        # text_2_part2 = MathTex(r"\text{Vector length is }",r"0",color=dark_pink
        # ).scale(1.3)
        # text_2 = VGroup(text_2_part1, text_2_part2).arrange(DOWN,buff=0.5).to_edge(LEFT).shift(RIGHT+UP)
        # # text_2[2:].shift(1*LEFT)
        # arrow_0_0_down = CurvedArrow(
        #     start_point=text_2.get_corner(UR)+0.2*DOWN+0.3*RIGHT,
        #     end_point=text_2.get_corner(DR)+0.2*UP+0.3*RIGHT,
        #     angle=-PI/2,
        #     color=light_pink,
        # )
        # self.play(
        #     FadeTransform(text_1,text_2[0:2]),
        # )

        # text_2_formula_1 = MathTex(r" \sqrt{0^2 + 0^2}",color=dark_pink
        # ).next_to(norm2_2d,DOWN)
        # # text_2_formula_1[1].set_color(dark_pink)
        # # text_2_formula_1[3].set_color(dark_pink)
        
        # text_2_formula_2 = MathTex(r" = ",r"0",color=dark_pink
        # ).next_to(text_2_formula_1,RIGHT).shift(0*DOWN)
        # self.play(
        #     FadeOut(vector,run_time=0.5),
        #     tip.animate.move_to(axes.c2p(0,0)),
        #     # TransformFromCopy(norm2_2d[1:],text_2_formula_1),
        #     # Write(text_2_formula_2),
        # )
        # self.wait(1)
        # self.play(
        #     Create(arrow_0_0_down),
        #     Write(text_2[2:]),
        # )
        # self.wait(1)
        # arrow_0_0_up = CurvedArrow(
        #     start_point=text_2.get_corner(DL)+0.2*UP+0.3*LEFT,
        #     end_point=text_2.get_corner(UL)+0.3*DOWN+0.3*LEFT,
        #     angle=-PI/2,
        #     color=light_pink,
        # )
        # self.play(
        #     Create(arrow_0_0_up),
        # )
        # self.wait(4)

        # self.play(
        #     FadeOut(arrow_0_0_up),
        #     FadeOut(arrow_0_0_down),
        #     FadeOut(text_2),
        #     # FadeOut(text_2_formula_1),
        #     # FadeOut(text_2_formula_2),
        #     FadeIn(vector),
        #     tip.animate.move_to(axes.c2p(6,4)),
        #     run_time=1
        # )

        # # 3

        # text_3_part1 = MathTex(r"t \cdot ",r"\text{Vector}",color=dark_pink
        # ).scale(1.3).to_edge(LEFT).shift(2*RIGHT+UP)
        # text_3_part2 = MathTex(r"t \cdot ",r"\text{Vector length}",color=dark_pink
        # ).scale(1.3).to_edge(LEFT).shift(RIGHT+0.9*DOWN)
        # self.play(
        #     Write(text_3_part1),
        # )
        # self.wait(1)
        # note_text = MathTex(r"t \cdot (x,y) = (t \times x , t \times y )",color=light_purple).move_to(text_3_part1.get_center()+0.6*UP)
        # # self.play(
        # #     Write(note_text),
        # #     run_time=2.5
        # # )
        # # self.wait(2)
        
        # # -----------------------------------
        # # STEP 0: Original norm
        # # -----------------------------------
        # norm = MathTex(
        #     # r"=",
        #     r"\sqrt{",
        #     r"(x)^2",
        #     r"+",
        #     r"(y)^2",
        #     r"}",
        #     color=light_purple
        # ).next_to(norm2_2d, DOWN)

        # self.play(Write(norm))

        # # -----------------------------------
        # # STEP 1: x,y  →  tx,ty
        # # -----------------------------------
        # scaled = MathTex(
        #     # r"=",
        #     r"\sqrt{",
        #     r"(tx)^2",
        #     r"+",
        #     r"(ty)^2",
        #     r"}",
        #     color=light_purple
        # ).move_to(norm)

        # self.play(
        #     TransformMatchingTex(norm, scaled) #, transform_mismatches=True
        # )

        # # -----------------------------------
        # # STEP 2: Expand powers
        # # -----------------------------------
        # expanded = MathTex(
        #     # r"=",
        #     r"\sqrt{ (",
        #     r"t^2",r"x^2)",
        #     r"+ (",
        #     r"t^2",r"y^2)",
        #     r"}",
        #     color=light_purple
        # ).move_to(scaled)

        # self.play(
        #     TransformMatchingTex(scaled, expanded)
        # )

        # # -----------------------------------
        # # STEP 3: Highlight common factor
        # # -----------------------------------
        # expanded.set_color_by_tex("t^2", dark_orange)

        # # -----------------------------------
        # # STEP 4: Factor t^2
        # # -----------------------------------
        # factored = MathTex(
        #     # r"=",
        #     r"\sqrt{",
        #     r"t^2",
        #     r"(x^2 + y^2)",
        #     r"}",
        #     color=light_purple
        # ).move_to(expanded).set_color_by_tex("t^2", dark_orange)

        # self.play(
        #     TransformMatchingTex(expanded, factored)
        # )

        # # -----------------------------------
        # # STEP 5: Move sqrt(x^2+y^2) forward
        # # -----------------------------------
        # reordered = MathTex(
        #     # r"=",
        #     r"\sqrt{t^2}",
        #     r"\sqrt{x^2 + y^2}",
        #     color=light_purple
        # ).move_to(factored)

        # self.play(
        #     TransformMatchingTex(factored, reordered)
        # )

        # # -----------------------------------
        # # STEP 6: t^2 leaves sqrt and becomes |t|
        # # -----------------------------------
        # final = MathTex(
        #     # r"=",
        #     r"|t|",
        #     r"\sqrt{x^2 + y^2}",
        #     color=light_purple
        # ).move_to(reordered)

        # self.play(
        #     TransformMatchingTex(reordered, final)
        # )
        # final[1].set_color(light_orange)
        # length_text = MathTex(r"\text{Vector length}",color=light_orange
        # ).next_to(final[0],RIGHT)
        # self.play(
        #     ReplacementTransform(final[1],length_text)
        # )

        # arrow_0_0_up = CurvedArrow(
        #     start_point=text_3_part1.get_corner(DR)+0.1*UP+0.6*RIGHT,
        #     end_point=text_3_part2.get_corner(UR)+0.1*DOWN+0.6*RIGHT,
        #     angle=-PI/2,
        #     color=light_pink,
        # )
        # text_3_part2_2 = MathTex(r"|t| \cdot ",r"\text{Vector length}",color=dark_pink
        # ).scale(1.3).to_edge(LEFT).shift(RIGHT+0.6*DOWN)
        # self.play(
        #     Create(arrow_0_0_up),
        #     Write(text_3_part2_2),
        # )
        # self.wait(1)

        # self.play(
        #     FadeOut(final[:2]),
        #     FadeOut(length_text),
        #     FadeOut(norm2_2d),
        #     # FadeOut(note_text),
        # )

        # lambda_text = MathTex("|t| < 1",color=BLACK).scale(1.6).move_to(text_3_part2.get_center()+2*DOWN+LEFT)
        # self.play(
        #     Write(lambda_text)
        # )
        # vector_lower = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(3,2),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # VECTOR_COPY = vector.copy()

        # self.play(
        #     Transform(vector, vector_lower)
        # )

        # self.wait(2)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # # | lambda | > 1

        # lambda_text_2 = MathTex("|t| > 1",color=BLACK).scale(1.6).move_to(text_3_part2.get_center()+2*DOWN+LEFT)
        # self.play(
        #     FadeTransform(lambda_text, lambda_text_2),
        # )
        # vector_higher = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(7.5,5),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Transform(vector, vector_higher)
        # )

        # self.wait(2)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # # lambda < 0 (negative)

        # lambda_text_3 = MathTex("t < 0",color=BLACK).scale(1.6).move_to(text_3_part2.get_center()+2*DOWN+LEFT)
        # self.play(
        #     FadeTransform(lambda_text_2, lambda_text_3),
        # )

        # vector_higher = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(-6,-4),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Transform(vector, vector_higher)
        # )

        # self.wait(2)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # self.play(
        #     FadeOut(text_3_part1),
        #     FadeOut(text_3_part2_2),
        #     FadeOut(lambda_text_3),
        #     FadeOut(arrow_0_0_up),
        #     FadeOut(tip_text),
        # )
        
        # # 4

        # text_4 = MathTex(r"\text{Triangle Inequality}",color=dark_pink
        # ).scale(1.3).to_edge(LEFT).shift(RIGHT+1.7*UP)

        # self.play(
        #     Write(text_4),
        #     # FadeOut(norm2_2d),
        # )
        # self.wait(1)

        # vector_rule3_1 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(2,3),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_red,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_x = MathTex(r"\vec{a}").set_color(BLACK).move_to(vector_rule3_1.get_center()+0.4*UP)

        # vector_rule3_2 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(4,1),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_y = MathTex(r"\vec{b}").set_color(BLACK).move_to(vector_rule3_2.get_center()+0.3*DOWN)

        # self.play(
        #     FadeOut(VGroup(tip,vector)),
        #     GrowArrow(vector_rule3_1, run_time=1.0, rate_func=rush_from),
        #     Write(text_x),
        #     GrowArrow(vector_rule3_2, run_time=1.0, rate_func=rush_from),
        #     Write(text_y),
        # )

        # dot_arrow_1 =  DashedLine(
        #     start=axes.c2p(2,3),
        #     end=axes.c2p(6,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_green,
        # )

        # dot_arrow_2 =  DashedLine(
        #     start=axes.c2p(4,1),
        #     end=axes.c2p(6,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_red,
        # )

        # self.play(
        #     Create(dot_arrow_1),
        #     Create(dot_arrow_2),
        #     FadeIn(tip)
        # )
        # self.wait(0.5)

        # vector_rule3_3 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,4),
        #     buff=0,
        #     stroke_width=6,
        #     color=BLACK,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # text_x_plus_y = MathTex(r"\vec{a} + \vec{b}").set_color(BLACK).move_to(vector_rule3_3.get_center()+0.47*UP)
        # self.play(
        #     GrowArrow(vector_rule3_3, run_time=1.0, rate_func=rush_from),
        #     Write(text_x_plus_y),
        # )

        # self.play(
        #     FadeOut(axes),
        #     FadeOut(dot_arrow_1),
        #     FadeOut(dot_arrow_2),
        #     FadeOut(tip),
        # )
        # self.wait(1)

        # vector_rule3_1_group = VGroup(vector_rule3_1,text_x)
        # self.play(
        #     vector_rule3_1_group.animate.move_to(dot_arrow_2.get_center()),
        #     text_x.animate.shift(dot_arrow_2.get_center()+0.01*RIGHT),
        #     run_time=1
        # )

        # triangle = Polygon(
        #     vector_rule3_1.get_end(),
        #     vector_rule3_2.get_end(),
        #     vector_rule3_3.get_start(),
        # )

        # triangle.set_stroke(color=dark_orange, width=7)
        # triangle.set_fill(light_orange, opacity=0.3)

        # self.play(
        #     DrawBorderThenFill(triangle,2),
        #     run_time=1
        # )
        # self.play(
        #     triangle.animate.set_opacity(0),
        #     run_time=0.5
        # )

        # self.play(
        #     FadeOut(triangle),
        #     FadeOut(text_x_plus_y),
        #     FadeOut(text_x),
        #     FadeOut(text_y),
        # )

        # vectors_for_transform = VGroup(vector_rule3_1, vector_rule3_2)
        # vector_merged = vector.copy().set_color(dark_red)
        # vector_merged.shift(0.5*UP+0.1*LEFT).scale(( vector_rule3_1.get_length() + vector_rule3_2.get_length() )/( vector.get_length() ))

        # text_1 = MathTex(r" \text{length } (\vec{a} + \vec{b}) ").set_color(BLACK).move_to(vector.get_center()+0.7*DOWN+0.5*RIGHT)
        # text_2 = MathTex(r" \text{length } \vec{a} + \text{length } \vec{b} ").set_color(BLACK).move_to(vector_merged.get_center()+0.7*UP+1.2*LEFT)

        # self.play(
        #     FadeTransform(vectors_for_transform, vector_merged),
        #     FadeIn(text_1),
        #     FadeIn(text_2),
        # )

        # self.wait(1)

        # vector.set_color(BLACK)
        # self.play(
        #     FadeOut(plane),
        #     # FadeOut(norm2_2d),
        #     FadeOut(text_2),
        #     FadeOut(text_1),
        #     FadeOut(vector_rule3_3),
        #     FadeOut(vector),
        #     FadeOut(vector_merged),
        #     FadeOut(text_4),
        # )

        # self.wait(2)

        # # self.wait(1)
        # self.play(
        #     *[FadeOut(mob) for mob in self.mobjects]
        # )
        # self.wait(1)

        return plane,axes

    def scene4_subScene1(self,title,plane,axes):

        self.play(
            FadeIn(plane),
            FadeIn(axes),
        )

        # 1

        # manhatan_arrow = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,6),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_orange,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_x = MathTex(r"\vec{x}").set_color(BLACK).move_to(manhatan_arrow.get_center()+0.4*UP)

        # self.play(
        #     GrowArrow(manhatan_arrow, run_time=1.0, rate_func=rush_from),
        #     Write(text_x),
        #     run_time=1
        # )

        # dot_arrow_x =  DashedLine(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,0), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_green,
        #     stroke_width=10,
        # )
        # text_dot_x = MathTex(r"x_1").set_color(BLACK).move_to(dot_arrow_x.get_center()+0.4*DOWN)

        # dot_arrow_y =  DashedLine(
        #     start=axes.c2p(6,0),
        #     end=axes.c2p(6,6), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_red,
        #     stroke_width=10,
        # )
        # text_dot_y = MathTex(r"x_2").set_color(BLACK).move_to(dot_arrow_y.get_center()+0.4*RIGHT)

        # sum_norm_text = MathTex(r"x_1 + x_2",color=BLACK
        # ).move_to(text_x.get_center()+0.7*LEFT)

        # tip_start = Dot(axes.c2p(0,0), color=dark_red, radius=0.1)        
        # tip_end = Dot(axes.c2p(6,6), color=dark_red, radius=0.1)
        # self.play(
        #     FadeIn(tip_start),
        #     FadeIn(tip_end)
        # )
        # self.wait(1)


        # self.play(
        #     Create(dot_arrow_x),
        #     Write(text_dot_x),
        # )
        # self.play(
        #     Create(dot_arrow_y),
        #     Write(text_dot_y),
        # )
        # self.play(
        #     TransformMatchingTex(text_x, sum_norm_text),
        # )

        # self.play(
        #     FadeOut(manhatan_arrow),
        #     FadeOut(dot_arrow_x),
        #     FadeOut(text_dot_x),
        #     FadeOut(dot_arrow_y),
        #     FadeOut(text_dot_y),
        #     FadeOut(sum_norm_text),
        #     FadeOut(tip_start),
        #     FadeOut(tip_end),
        # )

        # 2

        manhatan_arrow_2 = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(-6,-4),
            buff=0,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        text_x = MathTex(r"\vec{x}").set_color(BLACK).move_to(manhatan_arrow_2.get_center()+0.4*DOWN)

        self.play(
            GrowArrow(manhatan_arrow_2, run_time=1.0, rate_func=rush_from),
            Write(text_x),
            run_time=1
        )

        dot_arrow_x =  DashedLine(
            start=axes.c2p(0,0),
            end=axes.c2p(-6,0), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_green,
            stroke_width=10,
        )
        text_dot_x = MathTex(r"x_1").set_color(BLACK).move_to(dot_arrow_x.get_center()+0.4*UP)

        dot_arrow_y =  DashedLine(
            start=axes.c2p(-6,0),
            end=axes.c2p(-6,-4), 
            dash_length=0.2, 
            dashed_ratio=0.5, 
            color=dark_red,
            stroke_width=10,
        )
        text_dot_y = MathTex(r"x_2").set_color(BLACK).move_to(dot_arrow_y.get_center()+0.4*LEFT)

        sum_norm_text = MathTex(r"|x_1| + |x_2|",color=BLACK
        ).move_to(text_x.get_center()+0.7*RIGHT)

        tip_start = Dot(axes.c2p(0,0), color=dark_red, radius=0.1)
        tip_end = Dot(axes.c2p(-6,-4), color=dark_red, radius=0.1)
        self.play(
            FadeIn(tip_start),
            FadeIn(tip_end)
        )

        self.play(
            Create(dot_arrow_x),
            Write(text_dot_x),
        )
        self.play(
            Create(dot_arrow_y),
            Write(text_dot_y),
        )

        self.play(
            TransformMatchingTex(text_x, sum_norm_text),
            run_time=1
        )
        self.wait(1)

        # num example
        # text_num_x = MathTex(r"-4",color=dark_pink).move_to(text_dot_x.get_center())
        # text_num_y = MathTex(r"-3",color=dark_pink).move_to(text_dot_y.get_center()+0.1*LEFT)
        # text_length_vector_1 = MathTex(r"|-4| + |-3|",color=dark_pink).move_to(manhatan_arrow_2.get_center()+1.7*RIGHT)
        # text_length_vector_2part0 = MathTex(r"4 + 3",color=dark_pink).move_to(manhatan_arrow_2.get_center()+1*RIGHT)
        # text_length_vector_2part1 = MathTex(r"7",color=dark_pink).move_to(text_length_vector_2part0.get_center())
        # self.play(
        #     FadeOut(text_dot_x),
        #     FadeIn(text_num_x)
        # )
        # self.wait(0.5)
        # self.play(
        #     FadeOut(text_dot_y),
        #     FadeIn(text_num_y)
        # )
        # self.wait(0.5)
        # self.play(
        #     FadeTransform(sum_norm_text,text_length_vector_1),
        # )
        # self.wait(1)
        # self.play(
        #     FadeTransform(text_length_vector_1,text_length_vector_2part0),
        # )
        # self.wait(0.7)
        # self.play(
        #     FadeTransform(text_length_vector_2part0,text_length_vector_2part1),
        # )
        # self.wait(1)
       
        # self.play(
        #     FadeOut(text_num_x),
        #     FadeIn(text_dot_x),
        #     FadeOut(text_num_y),
        #     FadeIn(text_dot_y),
        #     FadeOut(text_length_vector_2part1),
        # )
        # self.wait(1)


        norm1_2d = MathTex(
            r"\text{length}_{\text{Manhattan}}",r"= ",r"|x_1| + |x_2|",color=BLACK
        ).scale(2).move_to(axes.c2p(0,3))
        self.play(
            Write(norm1_2d),
        )
        self.wait(1)

        self.play(
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(tip_start),
            FadeOut(tip_end),
            FadeOut(manhatan_arrow_2),
            FadeOut(sum_norm_text),
            FadeOut(dot_arrow_x),
            FadeOut(text_dot_x),
            FadeOut(dot_arrow_y),
            FadeOut(text_dot_y),
            FadeOut(norm1_2d),
        )

    def scene4_subScene2(self,title):
        "scene4 : subScene2 : norm definition"
        
        question_tex = MathTex("\\text{ What happens if we try to generalize this? }").set_color(BLACK)
        question_group, question_box, image_1, image_2 = self.ask_question(question_tex,True,True)

        group_GroupBoxQuetion = VGroup(question_group,question_box)
        group_GroupBoxQuetion.shift(1.5*UP)
        # image_1.scale(1.2).shift(3.5*DOWN)
        # self.add()
        self.play(
            # FadeIn(image_1),
            FadeIn(group_GroupBoxQuetion)
        )
        self.wait(11)
        # self.play(
        #     FadeOut(group_GroupBoxQuetion),
        # )
        # self.wait(0.5)

        def_norm_line1 = MathTex(
            r"\text{A norm on } X \text{ is a function }",
            r"\|\cdot\| : X \to \mathbb{R}"
        ).set_color(BLACK)

        def_norm_line2 = MathTex(
            r"\text{satisfying}"
        ).set_color(BLACK)

        # def_norm_line3 = MathTex(
        #     r"\begin{aligned}",
        #     # r"1.& \quad \|x\| \ge 0 \\"
        #     r"1.& \quad \|x\| = 0 \iff x = 0 \\",
        #     r"2.& \quad \|\lambda x\| = |\lambda| \, \|x\| \\",
        #     r"3.& \quad \|x + y\| \le \|x\| + \|y\|",
        #     r"\end{aligned}"
        # ).set_color(BLACK).scale(0.85)

        line1_3 = MathTex(r"N1.\quad \|x\| = 0 \iff x = 0")
        line2_3 = MathTex(r"N2.\quad \|\lambda x\| = |\lambda| \, \|x\|")
        line3_3 = MathTex(r"N3.\quad \|x + y\| \le \|x\| + \|y\|")
        def_norm_line3 = VGroup(line1_3, line2_3, line3_3).arrange(DOWN, aligned_edge=LEFT, buff=0.4).set_color(BLACK).scale(0.9)

        def_norm_line4 = MathTex(r"\quad \text{for all } x,y \in X \text{ and } \lambda \in \mathbb{K}.").set_color(BLACK)

        def_norm = VGroup(def_norm_line1, def_norm_line2, def_norm_line3,def_norm_line4).arrange(DOWN, buff=0.3).scale(0.9)

        def_norm.next_to(title.get_center(), DOWN)

        norm_group, norm_box = self.show_definition(def_norm, title,True)
        norm_group.shift(1.5*UP)
        norm_box.move_to(norm_group.get_center())
        norm_box_and_text_group = VGroup(norm_group,norm_box)
        norm_box_and_text_group.scale(1.2)

        # norm title
        norm_title = MathTex(r"\text{NORM}", color=BLACK, font_size=80).move_to(title.get_center())
        
        self.play(
            TransformMatchingShapes(group_GroupBoxQuetion, norm_box), 
            Write(norm_title),
            FadeOut(image_1),
            # FadeOut(image_2),
            Write(norm_group),
            run_time=1
        )
        image_2.shift(9*LEFT)
        self.add(image_2)

        self.wait(4)
        for line in [line1_3, line2_3, line3_3]:
            rect = SurroundingRectangle(
                line,
                color=dark_red,      
                buff=0.2,  
                fill_opacity=0,
                stroke_width=3,
                corner_radius=0.15,
            )
            self.play(
                Create(rect), 
            )
            self.wait(1.5)
            self.play(
                Uncreate(rect), 
            )

        self.wait(2)
        
        self.play(
            Uncreate(norm_box),
            FadeOut(norm_group),
            FadeOut(image_2),
        )

        return norm_group, norm_box, question_group, question_box, norm_title

    def scene4_subScene1_part2(self,title,):
        point_text = MathTex(r"\vec{x} = (x_1,x_2)",color=BLACK).move_to(title.get_center()+0.5*DOWN)

        norm1 = MathTex(r"\text{length }_{\text{Manhattan} }(\vec{x})",r" = |x_1| + |x_2|",color=dark_orange).scale(1.5).move_to(point_text.get_center()+1*DOWN)
        norm1_2 = MathTex(r"\text{length }_{\text{Manhattan} }(\vec{x})",r" = |x_1|^1 + |x_2|^1",color=dark_orange).scale(1.5).move_to(norm1.get_center())
        norm1_3 = MathTex(r"\text{length }_{\text{Manhattan} }(\vec{x})",r" = (|x_1|^1 + |x_2|^1)^\frac{1}{1} ",color=dark_orange).scale(1.5).move_to(norm1_2.get_center())
        norm1_3_compare = MathTex(
            r"\text{length }_{\text{Manhattan}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^1",
            r"+",
            r"|x_2|", r"^1",
            r")^{", r"\frac{1}{1}", r"}",
            color=dark_orange,
        ).scale(1.5).move_to(norm1_2.get_center())
        common_color = dark_green
        norm1_3_compare.set_color_by_tex("|x_1|", common_color)
        norm1_3_compare.set_color_by_tex("|x_2|", common_color)
        norm1_3_compare.set_color_by_tex("+", common_color)
        norm1_3_compare.set_color_by_tex("(", common_color)
        norm1_3_compare.set_color_by_tex(")", common_color)
        # norm1_3_compare.set_color_by_tex("}", common_color)

        norm2 = MathTex(r"\text{length }_{\text{Euclid} }(\vec{x})",r" = \sqrt{x_1^2 + x_2^2 }",color=dark_pink).scale(1.2).move_to(norm1_3.get_center()+1.2*DOWN)  #Pythagoras
        norm2_2 = MathTex(r"\text{length }_{\text{Euclid} }(\vec{x})",r" = \sqrt{|x_1|^2 + |x_2|^2 }",color=dark_pink).scale(1.5).move_to(norm2.get_center())
        norm2_3 = MathTex(r"\text{length }_{\text{Euclid} }(\vec{x})",r" = (|x_1|^2 + |x_2|^2)^\frac{1}{2} ",color=dark_pink).scale(1.5).move_to(norm2_2.get_center())
        norm2_3_compare = MathTex(
            r"\text{length }_{\text{Euclid}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^2",
            r"+",
            r"|x_2|", r"^2",
            r")^{", r"\frac{1}{2}", r"}",
            color=dark_pink,
        ).scale(1.5).move_to(norm2_2.get_center())
        common_color = dark_green
        norm2_3_compare.set_color_by_tex("|x_1|", common_color)
        norm2_3_compare.set_color_by_tex("|x_2|", common_color)
        norm2_3_compare.set_color_by_tex("+", common_color)
        norm2_3_compare.set_color_by_tex("(", common_color)
        norm2_3_compare.set_color_by_tex(")", common_color)
        # norm2_3_compare.set_color_by_tex("}", common_color)

        norm3 = MathTex(
            r"\text{length }_{\text{?}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^3",
            r"+",
            r"|x_2|", r"^3",
            r")^{", r"\frac{1}{3}", r"}",
            color=dark_red,
        ).scale(1.5).move_to(norm2_3_compare.get_center()+1*DOWN+1.2*RIGHT)
        common_color = dark_green
        norm3.set_color_by_tex("|x_1|", common_color)
        norm3.set_color_by_tex("|x_2|", common_color)
        norm3.set_color_by_tex("+", common_color)
        norm3.set_color_by_tex("(", common_color)
        norm3.set_color_by_tex(")", common_color)

        norm4 = MathTex(
            r"\text{length }_{\text{?}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^4",
            r"+",
            r"|x_2|", r"^4",
            r")^{", r"\frac{1}{4}", r"}",
            color=dark_red,
        ).scale(1.5).move_to(norm2_3_compare.get_center()+1*DOWN+1.2*RIGHT)
        common_color = dark_green
        norm4.set_color_by_tex("|x_1|", common_color)
        norm4.set_color_by_tex("|x_2|", common_color)
        norm4.set_color_by_tex("+", common_color)
        norm4.set_color_by_tex("(", common_color)
        norm4.set_color_by_tex(")", common_color)

        # normp = MathTex(r"\text{length }_{\text{p} }(\vec{x})",r" = (|x_1|^p + |x_2|^p)^\frac{1}{p} ",color=dark_red).scale(1.5).move_to(norm2_3.get_center()+1*DOWN)
        normp = MathTex(
            r"\text{length }_{\text{p}}(\vec{x}) = ",
            r"(",
            r"|x_1|", r"^p",
            r"+",
            r"|x_2|", r"^p",
            r")^{", r"\frac{1}{p}", r"}",
            color=dark_red,
        ).scale(1.5).move_to(norm2_3_compare.get_center()+1*DOWN+1.2*RIGHT)
        common_color = dark_green
        normp.set_color_by_tex("|x_1|", common_color)
        normp.set_color_by_tex("|x_2|", common_color)
        normp.set_color_by_tex("+", common_color)
        normp.set_color_by_tex("(", common_color)
        normp.set_color_by_tex(")", common_color)

        p_ge_1 = MathTex(r"p \ge 1",color=BLACK)
        text_group,box = self.show_minorPoint(p_ge_1,True)
        text_group.move_to(normp.get_center()+2*DOWN+RIGHT)
        box.move_to(text_group.get_center())

        VGroup(point_text,norm1,norm2, VGroup(normp, VGroup(text_group, box)).arrange(RIGHT,buff=0.3)).arrange(DOWN,buff=0.4).shift(0.7*UP)
        norm1_2.move_to(norm1.get_center())
        norm1_3.move_to(norm1.get_center())
        norm1_3_compare.move_to(norm1_3.get_center())
        norm2_2.move_to(norm2.get_center())
        norm2_3.move_to(norm2.get_center())
        norm2_3_compare.move_to(norm2_3.get_center())
        
        self.play(
            Write(point_text),
        )
        self.wait(5)
        self.play(
            Write(norm1),
        )
        self.play(
            TransformMatchingTex(norm1,norm1_2),
        )
        self.play(
            TransformMatchingTex(norm1_2,norm1_3),
        )
        self.wait(5)

        self.play(
            Write(norm2),
        )
        self.play(
            TransformMatchingTex(norm2,norm2_2),
        )
        self.play(
            TransformMatchingTex(norm2_2,norm2_3),
        )
        self.wait(8)

        self.play(
            TransformMatchingTex(norm1_3,norm1_3_compare),
            TransformMatchingTex(norm2_3,norm2_3_compare),
        )

        # image_think = ImageMobject("images/think_img.png").scale(2).to_edge(DL).shift(3.5*LEFT+1.1*DOWN)
        # self.add(image_think)
        self.wait(14)

        # self.play(
        #     Write(norm3),
        # )
        # self.wait(1)
        # self.play(
        #     TransformMatchingTex(norm3,norm4),
        # )
        # self.wait(1)

        # find_img = ImageMobject("images/find_img.png").scale(2).to_edge(DL).shift(3.5*LEFT+1.4*DOWN)
        # self.play(
        #     FadeOut(image_think),
        # )
        # self.add(find_img)

        self.play(
            # find_img.animate.scale(0.7).shift(0.5*DOWN),
            # TransformMatchingTex(norm4,normp),
            Write(normp),
            run_time=1
        )
        self.wait(1)

        
        self.play(
            Create(box),
            Write(text_group),
        )
        self.wait(17)

        self.play(
            FadeOut(text_group),
            FadeOut(box),
            # FadeOut(find_img),
            FadeOut(normp),
            FadeOut(norm1_3_compare),
            FadeOut(norm2_3_compare),
            FadeOut(point_text),
            # FadeOut(),
        )

        self.wait(1)

    def scene4_subScene3(self, title):
        # draw number plane as background
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]+DOWN)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 7, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN)
        self.play(
            Create(plane),
            Create(axes)
        )
        self.wait(0.5)

        # dot at tip of vector
        tip = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        self.play(FadeIn(tip))

        # draw vector in (0,0)
        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(GrowArrow(vector, run_time=1, rate_func=rush_from))
        self.wait(0.5)

        # draw brace
        brace = BraceBetweenPoints(vector.get_start()+ UP*0.2, vector.get_end() + UP*0.2, rotate_vector(vector.get_unit_vector(), PI/2) ).set_color("#000000")
        self.play(GrowFromCenter(brace, run_time=0.8))

        # add norm text
        norm_text = brace.get_text("Norm").set_color(BLACK)
        self.play(FadeIn(norm_text, shift=UP*0.2))
        self.wait(0.5)

        # add "= Vector Length" and "= distance to the origin"
        vector_dis_text = MathTex(" \\text{ distance to the origin } = ").set_color(BLACK)
        vector_dis_text.next_to(norm_text, LEFT, buff=0.3)
        self.play(FadeIn(vector_dis_text))  #  norm_text.animate.shift(UP*0.2), 
        self.wait(1)

        vector_length_text = MathTex(" \\text{Vector Length} = ").set_color(BLACK)
        vector_length_text.next_to(norm_text, LEFT, buff=0.3)
        self.play(TransformMatchingTex(vector_dis_text, vector_length_text))
        self.wait(1)

        # group texts
        norm_text_group = VGroup(norm_text, vector_length_text)

        self.play(
            FadeOut(norm_text_group),
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(tip),
            FadeOut(vector),
            FadeOut(brace),
        )
        self.wait(2)

        # blink effect
        # for _ in range(2):
        #     self.play(
        #         norm_text_group.animate.scale(1.5).set_color(dark_red),
        #         brace.animate.set_color(dark_red),
        #         rate_func=there_and_back,
        #         run_time=0.5
        #     )
        # 
        # self.wait(1)
        
        # vecor_name = MathTex("\\text{ x }").set_color(BLACK).move_to(norm_text.get_center())

        # self.play(
        #     TransformMatchingTex(norm_text_group,vecor_name)
        # )
        # self.wait(2)

        # rule1_text = MathTex("\quad \|x\| = 0 \iff x = 0").set_color(BLACK).scale(0.9)
        # rule2_text = MathTex("\quad \|\lambda x\| = |\lambda| \, \|x\|").set_color(BLACK).scale(0.9)
        # rule3_text = MathTex("\quad \|x + y\| \le \|x\| + \|y\|").set_color(BLACK).scale(0.9)

        # rule1_text.move_to(plane.get_edge_center(DOWN) + 1*RIGHT + 1*UP)
        # rule2_text.move_to(plane.get_edge_center(DOWN) + 1*RIGHT + 1*UP)
        # rule3_text.move_to(plane.get_edge_center(DOWN) + 1*RIGHT + 1*UP)

        # RULE 1
        # self.play(
        #     Write(rule1_text),
        #     FadeOut(brace),
        #     FadeOut(vecor_name),
        #     FadeOut(vector),
        #     tip.animate.move_to(axes.c2p(0,0)),
        #     run_time=1.0
        # )

        # self.wait(2)

        # RULE 2
        # self.play(
        #     TransformMatchingTex(rule1_text, rule2_text),
        #     tip.animate.move_to(axes.c2p(6,4)),
        #     GrowArrow(vector, run_time=1.0, rate_func=rush_from),
        #     run_time=1.0
        # )
        # self.wait(1)

        # # | lambda | < 1

        # lambda_text = MathTex("|\lambda| < 1",color=BLACK).scale(2).move_to(axes.get_center()+1*UP+3*LEFT)
        # self.play(
        #     Write(lambda_text)
        # )
        # vector_lower = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(3,2),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # VECTOR_COPY = vector.copy()

        # self.play(
        #     Transform(vector, vector_lower)
        # )

        # self.wait(1)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # # | lambda | > 1

        # lambda_text_2 = MathTex("|\lambda| > 1",color=BLACK).scale(2).move_to(axes.get_center()+1*UP+3*LEFT)
        # self.play(
        #     Unwrite(lambda_text),
        #     Write(lambda_text_2)
        # )
        # vector_higher = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(7.5,5),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Transform(vector, vector_higher)
        # )

        # self.wait(1)

        # self.play(
        #     Transform(vector, VECTOR_COPY)
        # )

        # self.wait(1)

        # # lambda < 0 (negative)

        # lambda_text_3 = MathTex("\lambda < 0",color=BLACK).scale(2).move_to(axes.get_center()+1*UP+3*LEFT)
        # self.play(
        #     Unwrite(lambda_text_2),
        #     Write(lambda_text_3)
        # )

        # vector_higher = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(-3,-2),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # self.play(
        #     Transform(vector, vector_higher)
        # )

        # self.wait(1)

        # self.play(
        #     Transform(vector, VECTOR_COPY),
        #     Unwrite(lambda_text_3)
        # )


        # # RULE 3

        # vector_rule3_1 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(2,3),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_red,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_x = MathTex("\\text{ x }").set_color(BLACK).move_to(vector_rule3_1.get_center()+0.4*UP)

        # vector_rule3_2 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(4,1),
        #     buff=0,
        #     stroke_width=6,
        #     color=dark_green,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )

        # text_y = MathTex("\\text{ y }").set_color(BLACK).next_to(vector_rule3_2, 0.35*DOWN, 0.1)

        # self.play(
        #     TransformMatchingTex(rule2_text, rule3_text),
        #     FadeOut(tip),
        #     FadeOut(vector),
        #     # FadeOut(vector_lower),
        #     # FadeOut(vector_higher),
        #     GrowArrow(vector_rule3_1, run_time=1.0, rate_func=rush_from),
        #     Write(text_x),
        #     GrowArrow(vector_rule3_2, run_time=1.0, rate_func=rush_from),
        #     Write(text_y),
        #     # run_time=1.0
        # )
        # self.wait(2)

        # dot_arrow_1 =  DashedLine(
        #     start=axes.c2p(2,3),
        #     end=axes.c2p(6,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_green,
        # )

        # dot_arrow_2 =  DashedLine(
        #     start=axes.c2p(4,1),
        #     end=axes.c2p(6,4), 
        #     dash_length=0.2, 
        #     dashed_ratio=0.5, 
        #     color=dark_red,
        # )

        # self.play(
        #     Create(dot_arrow_1),
        #     Create(dot_arrow_2),
        #     FadeIn(tip)
        # )
        # self.wait(2)

        # vector_rule3_3 = Arrow(
        #     start=axes.c2p(0,0),
        #     end=axes.c2p(6,4),
        #     buff=0,
        #     stroke_width=6,
        #     color=BLACK,
        #     tip_length=0.25,
        #     tip_shape=StealthTip
        # )
        # text_x_plus_y = MathTex("\\text{ x + y }").set_color(BLACK).move_to(vector_rule3_3.get_center()+0.4*UP)
        # self.play(
        #     GrowArrow(vector_rule3_3, run_time=1.0, rate_func=rush_from),
        #     Write(text_x_plus_y),
        # )

        # self.wait(2)

        # self.play(
        #     FadeOut(plane),
        #     FadeOut(axes),
        #     FadeOut(dot_arrow_1),
        #     FadeOut(dot_arrow_2),
        #     FadeOut(text_x_plus_y),
        #     FadeOut(text_x),
        #     FadeOut(text_y),
        #     FadeOut(tip),
        # )

        # vectors_for_transform = VGroup(vector_rule3_1, vector_rule3_2)
        # vector_merged = vector.copy().set_color(dark_red)
        # vector_merged.shift(0.5*UP+0.1*LEFT).scale(( vector_rule3_1.get_length() + vector_rule3_2.get_length() )/( vector.get_length() ))

        # text_1 = MathTex(" \|x + y\| ").set_color(BLACK).move_to(vector.get_center()+0.7*DOWN)
        # text_2 = MathTex(" \|x\| + \|y\| ").set_color(BLACK).move_to(vector_merged.get_center()+0.7*UP)

        # self.wait(0.7)

        # self.play(
        #     FadeTransform(vectors_for_transform, vector_merged),
        #     FadeIn(text_1),
        #     FadeIn(text_2),
        # )

        # self.wait(1)

        # vector.set_color(BLACK)
        # self.play(
        #     FadeOut(rule3_text),
        #     FadeOut(text_2),
        #     FadeOut(text_1),
        #     FadeOut(vector_rule3_3),
        #     FadeOut(vector),
        #     FadeOut(vector_merged),
        # )

    def scene4_subScene4(self,title):
        """scene 4 : sub scene 4 : prove and show ||x|| >= 0 """
        norm_title = MathTex(r"\text{NORM}", color=BLACK, font_size=80).move_to(title.get_center())
        self.add(norm_title)

        prove_text = MathTex("\|x\| \ge 0",color=BLACK).scale(1.3)
        text_group,box = self.show_conclusion(title, prove_text,True)
        self.play(
            Create(box),
            Write(text_group)
        )
        self.wait(2)

        conclusion_group = VGroup(text_group,box)
        self.play(
            conclusion_group.animate.shift(1.75*UP + 4.5*LEFT),
            run_time=1
        )

        # write proof
        proof_line1 = MathTex("\|x + y\| ","\le \|x\| + ","\|y\|",color=BLACK).scale(1.5).move_to(title.get_center()+0.9*DOWN+2*RIGHT)
        self.play(
            Write(proof_line1),
        )
        self.wait(0.5)

        variable_replacement = MathTex("y = -x",color=BLACK).scale(1.7).move_to(prove_text.get_center()+2*DOWN)
        self.play(
            Write(variable_replacement),
        )
        self.wait(0.5)
        proof_line1_variable_changed = MathTex("\|x + -x\| ","\le \|x\| + ","\|-x\|",color=BLACK).scale(1.5).move_to(title.get_center()+0.9*DOWN+2*RIGHT)
        self.play(
            TransformMatchingTex(proof_line1, proof_line1_variable_changed),
        )
        self.wait(0.5)

        part1_brace = Brace(proof_line1_variable_changed[0],DOWN,color=dark_orange)
        self.play(
            GrowFromCenter(part1_brace, run_time=0.8),
        )
        proof_line2_part1_initial = MathTex("\|0\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[0].get_center()+1.5*DOWN)
        self.play(
            Write(proof_line2_part1_initial),
        )
        self.wait(0.5)
        proof_line2_part1 = MathTex("0",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[0].get_center()+1.5*DOWN)
        self.play(
            FadeTransform(proof_line2_part1_initial,proof_line2_part1),
        )
        self.wait(0.5)

        part2_brace = Brace(proof_line1_variable_changed[2],DOWN,color=dark_orange)
        self.play(
            GrowFromCenter(part2_brace, run_time=0.8),
        )
        proof_line2_part2_initial = MathTex("|-1| \, \|x\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[2].get_center()+1.5*DOWN+0.2*RIGHT)
        self.play(
            Write(proof_line2_part2_initial),
        )
        self.wait(0.5)
        proof_line2_part2 = MathTex("\|x\|",color=BLACK).scale(1.5).move_to(proof_line1_variable_changed[2].get_center()+1.5*DOWN)
        self.play(
            FadeTransform(proof_line2_part2_initial, proof_line2_part2),
        )

        proof_line2_part3 = proof_line1_variable_changed[1].copy()
        self.play(
            proof_line2_part3.animate.shift(1.5*DOWN),
            run_time=1
        )

        
        proof_line2 = VGroup(proof_line2_part1, proof_line2_part3, proof_line2_part2)

        proof_line3 = MathTex("0 \le 2 \, \|x\|",color=BLACK).scale(1.5).move_to(proof_line2.get_center()+1.5*DOWN)
        self.play( 
            Write(proof_line3),
        )
        self.wait(0.5)

        proof_line4 = MathTex(r"0 \le \|x\| \quad . \blacksquare",color=BLACK).scale(1.5).move_to(proof_line3.get_center()+1.5*DOWN+0.5*RIGHT)
        square_for_end_proof = Square(0.5,color=BLACK).next_to(proof_line4,RIGHT)
        self.play( 
            Write(proof_line4),
        )

        # self.wait(0.5)

        # self.play(
        #     Create(square_for_end_proof),
        # )

        self.wait(1)

        self.play(
            FadeOut(proof_line1_variable_changed),
            FadeOut(variable_replacement),
            FadeOut(part1_brace),
            FadeOut(part2_brace),
            FadeOut(proof_line2),
            FadeOut(proof_line3),
            FadeOut(proof_line4),
            # FadeOut(square_for_end_proof),
        )

        # create shapes for better understanding
        
        # draw number plane as background
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]+DOWN+RIGHT)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 7, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+DOWN+RIGHT)
        self.play(
            Create(plane),
            Create(axes)
        )
        self.wait(0.5)

        # dot at tip of vector
        tip = Dot(axes.c2p(6,4), color=dark_red, radius=0.07)
        self.play(FadeIn(tip))

        # draw vector in (0,0)
        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(6,4),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        self.play(GrowArrow(vector, run_time=1.2, rate_func=rush_from))

        # draw brace
        brace = BraceBetweenPoints(vector.get_start()+ UP*0.2, vector.get_end() + UP*0.2, rotate_vector(vector.get_unit_vector(), PI/2) ).set_color("#000000")
        self.play(GrowFromCenter(brace, run_time=0.8))
        self.wait(0.5)

        # add norm text
        norm_text = brace.get_text("Norm").set_color(BLACK)
        self.play(FadeIn(norm_text, shift=UP*0.2))
        self.wait(0.5)

        # add "= Vector Length"
        vector_length_text = MathTex(" \\text{Vector Length} = ").set_color(BLACK)
        vector_length_text.next_to(norm_text, LEFT, buff=0.3)
        self.play(FadeIn(vector_length_text))
        self.wait(1)

        vector_group = VGroup(tip,vector,brace,norm_text,vector_length_text)

        vector_group.save_state()

        self.play(
            vector_group.animate.scale(0.01, about_point=axes.c2p(0,0)),
            run_time=3
        )
        self.play(
            Restore(vector_group),
            run_time=3
        )
        
        self.wait(2)

        self.play(
            FadeOut(vector_group),
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(conclusion_group),
            # FadeOut(),
            # FadeOut(),
            # FadeOut(),
            # FadeOut(),
        )

        self.wait(1)

    def scene4_subScene5(self,title):
        """scene 4: sub scene 5 : examples of norm"""

        # unit ball idea
        # nothing for now

        brain_img = ImageMobject("images/graduate_brain_img_mini.png").scale(2).to_corner(DL)
        # self.add(brain_img)

        # draw number plane as background
        plane = NumberPlane(
            y_range=[-6, 4, 1],
            x_range=[-4, 6, 1],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=7,
            x_length=7,
        ).move_to([0, 0, 0]+2.5*DOWN+2*RIGHT)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-6, 4, 1],
            y_length=7,
            x_range=[-4, 6, 1],
            x_length=7,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+2.5*DOWN+2*RIGHT)

        # example of norm

        vector_def = MathTex(
            r"\text{Let } \vec{x} = (x_1, \dots, x_n) \in \mathbb{R}^n.",color=BLACK
        ).to_corner(UL).shift(0.1*RIGHT+0.8*DOWN)

        # norm p
        normp_title = MathTex("p-Norm", color=dark_orange).next_to(vector_def,DOWN).shift(0.7*LEFT)

        normp_full_form = MathTex(
            r"\|\vec{x}\|_", r"p",
            r":=",
            r"(",
            r"|x_1|^", r"p",
            r"+",
            r"|x_2|^", r"p",
            r"+ \dots +",
            r"|x_n|^", r"p",
            r")^{\frac{1}{", r"p", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT).scale(1.2)

        normp_short_form = MathTex(
            r"=",
            r"\left(",
            r"\sum_{i=1}^{n} |x_i|^", r"p",
            r"\right)^{\frac{1}{", r"p", r"}}",
            color=BLACK
        ).next_to(normp_title,DOWN).shift(1.3*RIGHT+0.2*DOWN).scale(1.2)

        normp_full_form.set_color_by_tex("p", dark_pink)
        normp_short_form.set_color_by_tex("p", dark_pink)

        # norm 1
        condition_1 = Text("if p = 1", color=BLACK).move_to(normp_short_form.get_center())
        rect_1 = SurroundingRectangle(
            condition_1,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        norm1_title = MathTex("L1 Norm (Manhattan Norm)", color=dark_orange).move_to(normp_short_form.get_center()+DOWN)
        norm1_full_form = MathTex(
            r"\|\vec{x}\|_", r"\text{1}",
            r":=",
            r"(",
            r"|x_1|^", r"\text{1}",
            r"+",
            r"|x_2|^", r"\text{1}",
            r"+ \dots +",
            r"|x_n|^", r"\text{1}",
            r")^{\frac{1}{", r"\text{1}", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT).scale(1.2)
        norm1_full_form.set_color_by_tex(r"\text{1}", dark_pink)

        # norm 2
        condition_2 = Text("if p = 2", color=BLACK).move_to(normp_short_form.get_center())
        rect_2 = SurroundingRectangle(
            condition_2,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        norm2_title = MathTex("L2 Norm (Euclidean Norm)", color=dark_orange).move_to(norm1_title.get_center())
        norm2_full_form = MathTex(
            r"\|\vec{x}\|_", r"\text{2}",
            r":=",
            r"(",
            r"|x_1|^", r"\text{2}",
            r"+",
            r"|x_2|^", r"\text{2}",
            r"+ \dots +",
            r"|x_n|^", r"\text{2}",
            r")^{\frac{1}{", r"\text{2}", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT).scale(1.2)
        norm2_full_form.set_color_by_tex(r"\text{2}", dark_pink)

        # norm infinity
        condition_oo = MathTex(r"\text{if } p \to \infty", color=BLACK).scale(1.5).move_to(normp_short_form.get_center()+0.3*LEFT)
        rect_oo = SurroundingRectangle(
            condition_oo,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        normoo_title = MathTex(r"L \infty Norm (Maximum Norm)", color=dark_orange).move_to(norm1_title.get_center())
        normoo_limit = MathTex(
            r"\|\vec{x}\|_{\infty}",
            r"=",
            r"\lim_{", r"p", r"\to \infty}",
            r"\left(",
            r"\sum_{i=1}^{n}",
            r"|x_i|^", r"p",
            r"\right)^{\frac{1}{", r"p", r"}}",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT+0.15*UP).scale(1.2)
        normoo_limit.set_color_by_tex("p", dark_pink)

        norm_oo_short_form = MathTex(
            r"\|\vec{x}\|_{\infty}",
            r"=",
            r"\max_{1 \le i \le n}",
            r"|x_i|",
            color=BLACK
        ).next_to(normp_title,RIGHT).shift(2.7*LEFT+0.3*UP).scale(1.2)

        # vector name 
        self.wait(5)
        self.play(
            Write(vector_def)
        )
        self.wait(3)

        # norm p
        # self.play(
        #     Write(normp_title),
        # )
        # self.wait(0.6)
        self.play(
           Write(normp_full_form),
        )
        self.play(
            Write(normp_short_form),
        )
        self.wait(12)
        self.play(
            Unwrite(normp_short_form),
        )
        self.wait(1)

        # norm 1
        self.play(
            Create(rect_1),
            Write(condition_1),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(normp_full_form, norm1_full_form)
        )
        self.wait(1)

        # # create grid
        self.play(Create(plane))
        self.wait(0.5)
        self.play(Create(axes))
        self.wait(0.5)

        # norm 1 grid

        points_norm1 = [
            (3, 0),
            (0, 3),
            (-3, 0),
            (0, -3),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ]
        mid_points_norm1 = [
            (1, 0),    
            (0, 1),    
            (-1, 0),   
            (0, -1),   
            (2, 0),
            (1, 0),
            (-1, 0),    
            (-2, 0),
            (-2, 0),
            (-1, 0), 
            (1, 0),  
            (2, 0), 
        ]

        list_tip_2 = []

        for i in range(len(points_norm1)):
            point = points_norm1[i]
            mid_point = mid_points_norm1[i]

            # dot at tip of vector
            tip_2 = Dot(axes.c2p(*point), color=dark_red, radius=0.1)
            list_tip_2.append(tip_2)
            tip_1 = Dot(axes.c2p(*mid_point), color=dark_orange, radius=0.1)

            # draw vector in (0,0)
            vector_1 = Line(
                start=axes.c2p(0,0),
                end=axes.c2p(*mid_point),
                buff=0,
                stroke_width=10,
                color=dark_green,
            )

            vector_2 = Line(
                start=axes.c2p(*mid_point),
                end=axes.c2p(*point),
                buff=0,
                stroke_width=10,
                color=dark_green,
            )

            self.play(Create(vector_1),run_time=0.1) #, run_time=0.1, rate_func=rush_from
            self.play(FadeIn(tip_1),run_time=0.1)
            self.play(Create(vector_2),run_time=0.1)
            self.play(FadeIn(tip_2),run_time=0.1)

            # self.play(
            #     AnimationGroup(
            #         Create(vector_1),
            #         FadeIn(tip_1),
            #         lag_ratio=0.2
            #     )
            # )

            self.play(
                FadeOut(vector_1),
                FadeOut(tip_1),
                FadeOut(vector_2),
            )

        points_polygan = [
            axes.c2p(3, 0),
            axes.c2p(0, 3),
            axes.c2p(-3, 0),
            axes.c2p(0, -3),
        ]

        polygon = Polygon(
            *points_polygan,
            stroke_color=dark_terquise,
            stroke_width=4,
            fill_opacity=0
        )

        self.play(
            Create(polygon),
            rum_time=1
        )
        self.wait(1)

        self.play(
            FadeOut(VGroup(*list_tip_2)),
        )
        self.play(
            FadeOut(polygon),
        )

        # norm 2
        self.wait(2)
        self.play(
            TransformMatchingShapes(rect_1, rect_2),
            FadeTransform(condition_1, condition_2),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(norm1_full_form, norm2_full_form)
        )
        self.wait(1)

        # norm 2 grid

        vector = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(3,0),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        circle_static = Circle(radius=axes.x_axis.unit_size * 3,color=dark_terquise).move_to(axes.c2p(0,0))

        path = TracedPath(
            vector.get_end,
            stroke_color=dark_terquise,
            stroke_width=4
        )

        self.play(
            Create(vector, run_time=1, rate_func=rush_from),
        )

        self.play(
            Create(path),
            Create(circle_static),
            Rotate(
                vector,
                angle=TAU,
                about_point=axes.c2p(0,0)
            ),
            run_time=3,
            rate_func=linear
        )

        self.wait(1)

        self.play(
            FadeOut(vector),
            FadeOut(path),
            FadeOut(circle_static),
        )

        self.play(
            FadeOut(vector_def),

        )

        # norm inf

        self.play(
            TransformMatchingShapes(rect_2, rect_oo),
            FadeTransform(condition_2, condition_oo),
        )
        self.wait(1)
        self.play(
            TransformMatchingShapes(norm2_full_form, normoo_limit),
        )
        self.wait(2)
        self.play(
            TransformMatchingShapes(normoo_limit, norm_oo_short_form),
        )
        self.wait(2)

        # norm inf grid

        vector_1 = Line(
            start=axes.c2p(-3,3),
            end=axes.c2p(-3,-3),
            buff=0,
            stroke_width=5,
            color=dark_green,
        )
        vector_2 = Line(
            start=axes.c2p(-3,3),
            end=axes.c2p(3,3),
            buff=0,
            stroke_width=5,
            color=dark_purple,
        )
        vector_3 = Line(
            start=axes.c2p(3,-3),
            end=axes.c2p(3,3),
            buff=0,
            stroke_width=5,
            color=dark_pink,
        )
        vector_4 = Line(
            start=axes.c2p(3,-3),
            end=axes.c2p(-3,-3),
            buff=0,
            stroke_width=5,
            color=dark_orange,
        )

        # self.play(
        #     Create(vector_1),
        #     Create(vector_2),
        #     Create(vector_3),
        #     Create(vector_4),
        # )
        # self.wait(0.5)
        # self.play(
        #     Create(vector_2),
        # )
        # self.wait(0.5)
        # self.play(
        #     Create(vector_3),
        # )
        # self.wait(0.5)
        # self.play(
        #     Create(vector_4),
        # )
        # self.wait(0.5)

        squre = Polygon(
            *[axes.c2p(3,3), axes.c2p(3,-3), axes.c2p(-3,-3), axes.c2p(-3,3)],
            stroke_color=dark_terquise,
            stroke_width=4,
            fill_opacity=0
        )

        self.play(
            Create(squre),
            # FadeOut(VGroup(*[vector_1, vector_2, vector_3, vector_4])),
        )
        self.wait(2)

        self.play(
            FadeOut(squre),
            FadeOut(rect_oo),
            FadeOut(condition_oo),
            FadeOut(norm_oo_short_form),
        )

        plane2 = NumberPlane(
            y_range=[-6, 5, 3],
            x_range=[-5, 6, 3],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=7,
            x_length=7,
        ).move_to([0, 0, 0]+2*RIGHT)

        # draw axes on top
        axes2 = Axes(  # NumberLine
            y_range=[-6, 5, 3],
            y_length=7,
            x_range=[-5, 6, 3],
            x_length=7,
            axis_config={"color": dark_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]+2*RIGHT)

        self.play(
            TransformMatchingShapes(VGroup(plane, axes), VGroup(plane2, axes2)),
            run_time=1
        )
        self.play(2)

        circle_static = Circle(radius=axes2.x_axis.unit_size * 3,color=dark_terquise).move_to(axes2.c2p(0,0))

        text_p1 = MathTex(r"p = 1",color=dark_pink).move_to(brain_img.get_top()+2*UP).scale(2)
        rect_p1 = SurroundingRectangle(
            text_p1,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_p2 = MathTex(r"p = 2",color=dark_pink).move_to(brain_img.get_top()+2*UP).scale(2)
        rect_p2 = SurroundingRectangle(
            text_p2,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_pinf = MathTex(r"p \to \infty",color=dark_pink).move_to(brain_img.get_top()+2*UP).scale(2)
        rect_pinf = SurroundingRectangle(
            text_pinf,
            color=dark_red,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )

        points_polygan = [
            axes2.c2p(3, 0),
            axes2.c2p(0, 3),
            axes2.c2p(-3, 0),
            axes2.c2p(0, -3),
        ]

        polygon = Polygon(
            *points_polygan,
            stroke_color=dark_terquise,
            stroke_width=4,
            fill_opacity=0
        ).move_to(axes2.c2p(0,0))

        self.play(
            Write(text_p1),
            Create(rect_p1),
        )
        self.wait(1)
        norm1_name_text = MathTex(r"\text{Taxi Cab Norm}",color=dark_red).scale(1.5).next_to(rect_p1,UP).shift(0.7*RIGHT)
        norm2_name_text = MathTex(r"\text{Euclidean Norm}",color=dark_red).scale(1.5).next_to(rect_p1,UP).shift(0.8*RIGHT)
        normoo_name_text = MathTex(r"\text{Chebyshev Norm}",color=dark_red).scale(1.5).next_to(rect_p1,UP).shift(1*RIGHT)
        shape = polygon
        self.play(
            Create(shape),
            Write(norm1_name_text),
        )
        self.wait(2)

        # circle_static.shift(1.5*UP+1*LEFT)
        self.play(
            TransformMatchingTex(text_p1, text_p2),
            TransformMatchingShapes(rect_p1, rect_p2),
        )
        self.wait(1)
        self.play(
            Transform(shape, circle_static),
            TransformMatchingTex(norm1_name_text, norm2_name_text),
        )
        self.wait(2)

        squre = Polygon(
            *[axes2.c2p(3,-3), axes2.c2p(3,3), axes2.c2p(-3,3), axes2.c2p(-3,-3)],
            stroke_color=dark_terquise,
            stroke_width=4,
            fill_opacity=0
        ).move_to(axes2.c2p(0,0))
        self.play(
            TransformMatchingTex(text_p2, text_pinf),
            TransformMatchingShapes(rect_p2, rect_pinf),
        )
        self.wait(1)
        self.play(
            Transform(shape, squre),
            TransformMatchingTex(norm2_name_text, normoo_name_text),
        )
        self.wait(2)

        self.play(
            FadeOut(rect_pinf),
            FadeOut(text_pinf),
            FadeOut(shape),
            FadeOut(normoo_name_text),
            FadeOut(axes2),
            FadeOut(plane2),
            # FadeOut(brain_img),
        )
        self.wait(2)

    def scene4_subScene6(self, title):
        """ A normed space X is a vector space with a norm defined on it """
        text_normed_space = MathTex(r"\text{Normed space}",color=dark_green).move_to(title.get_center()+DOWN).scale(2)
        text_normed_space_parts = MathTex(r"( \, ",r"X",r" \, , \, ",r"\|.\|",r" \, )",color=dark_blue,arg_separator="  ").move_to(text_normed_space.get_center()+1.6*DOWN).scale(2)
        rect_x = SurroundingRectangle(
            text_normed_space_parts[1],
            color=dark_pink,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_vector_space = MathTex(r"\text{Vector space}",color=dark_pink).move_to(text_normed_space_parts.get_center()+2.6*DOWN+3*LEFT).scale(2)
        rect_vec_x = SurroundingRectangle(
            text_vector_space,
            color=dark_pink,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_x = CurvedArrow(
            start_point=text_normed_space_parts[1].get_left()+0.2*LEFT,
            end_point=rect_vec_x.get_top()+0.2*UP,
            angle=PI/2,
            stroke_width=6,
            color=dark_pink,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        rect_d = SurroundingRectangle(
            text_normed_space_parts[3],
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        text_distance = MathTex(r"\text{Norm}",color=dark_orange).move_to(text_normed_space_parts.get_center()+2.6*DOWN+3*RIGHT).scale(2)
        rect_distance = SurroundingRectangle(
            text_distance,
            color=dark_orange,        
            buff=0.2,          
            fill_opacity=0,    
            stroke_width=3,    
            corner_radius=0.15 
        )
        arrow_d = CurvedArrow(
            start_point=text_normed_space_parts[3].get_right()+0.2*RIGHT,
            end_point=rect_distance.get_top()+0.2*UP,
            angle=-PI/2,
            stroke_width=6,
            color=dark_orange,
            tip_length=0.25,
            tip_shape=StealthTip
        )

        self.play(
            Write(text_normed_space),
        )
        self.wait(2)
        self.play(
            Write(text_normed_space_parts[::2]),
        )
        self.wait(2)
        self.play(
            Write(text_normed_space_parts[1]),
            Create(rect_x),
            Create(arrow_x),
            Create(rect_vec_x),
            Write(text_vector_space),
        )
        self.wait(2)
        self.play(
            Write(text_normed_space_parts[3]),
            Create(rect_d),
            Create(arrow_d),
            Create(rect_distance),
            Write(text_distance),
        )
        self.wait(2)

        fade_out_list = [text_normed_space, text_normed_space_parts, rect_x, 
                         arrow_x, rect_vec_x, text_vector_space,
                         rect_d, arrow_d, rect_distance, text_distance]
        self.play(
            FadeOut(VGroup(*fade_out_list)),
        )

        self.wait(1)

    def scene4(self,title):
        """scene 4: what is norm ? """

        # self.play(
        #     Write(title),
        # )
        # self.play(
        #     FadeOut(title),
        # )
        # self.wait(1)

        # From Intuition to Mathematics
        # plane,axes = self.scene4_subScene0(title)

        # self.wait(1)

        # self.scene4_subScene1(title,plane,axes)

        # self.wait(1)

        # self.scene4_subScene1_part2(title)

        # self.wait(1)

        # norm definition
        # norm_group, norm_box, question_group, question_box, norm_title = self.scene4_subScene2(title)

        # shapes for norm definition
        # self.scene4_subScene3(title)

        # prove and show ||x||>=0
        # self.scene4_subScene4(title)

        # examples of norm
        # self.scene4_subScene5(title)

        # normed space
        self.scene4_subScene6(title)


    def scene3(self,topic_number,first_time=False):
        """scene 3: show topics list"""

        title = Tex(
            "Topics We Will Discuss In this Video ...",
            color=GOLD_A, font_size=60
        ).to_edge(UP)

        if first_time:

            bg_rect = Rectangle(
                width=10*config.frame_width, 
                height=10*config.frame_height, 
                stroke_width=0, 
                fill_color=topics_backGround_color, 
                fill_opacity=1
            )
            # self.add(bg_rect)
            # self.play(
            #     FadeIn(bg_rect, run_time=0.5),
            # )

            # self.play(
            #     Write(title),
            # )
            
            img = ImageMobject("images/topics.png")
            img.scale(1.1)

            self.play(
                FadeIn(bg_rect, run_time=0.5),
                FadeIn(img), 
            )

            self.camera.frame.save_state()


            # rect_1 = Rectangle(width=3.2, height=6.8).move_to(img.get_left() + RIGHT * 1.5 +0.2*UP).round_corners(radius=0.3)
            # rect_2 = Rectangle(width=3, height=6.8).move_to(img.get_left() + RIGHT * 4.7 +0.2*UP).round_corners(radius=0.3)
            # rect_3 = Rectangle(width=3, height=6.8).move_to(img.get_left() + RIGHT * 8.1 +0.2*UP).round_corners(radius=0.3)
            # rect_4 = Rectangle(width=4.5, height=6.8).move_to(img.get_left() + RIGHT * 12.2 +0.2*UP).round_corners(radius=0.3)

            rect_1 = Rectangle(width=3.2, height=6.8).move_to(img.get_left() + RIGHT * 1.5 +0.2*UP).round_corners(radius=0.3)
            rect_2 = Rectangle(width=3, height=6.8).move_to(img.get_left() + RIGHT * 4.55 +0.2*UP).round_corners(radius=0.3)
            rect_3 = Rectangle(width=5, height=6.8).move_to(img.get_left() + RIGHT * 8.1 +0.2*UP).round_corners(radius=0.3)
            rect_4 = Rectangle(width=3.5, height=6.8).move_to(img.get_left() + RIGHT * 12.1 +0.2*UP).round_corners(radius=0.3)


            zoom_rects = [rect_1, rect_2, rect_3, rect_4]
            wait_list = [ 7.7 , 6.1 , 6.7 , 8.1 ]
            # wait_list = [ 3.7 , 3.3 , 5.3 , 15.7 ]
            index_time = 0

            for rect in zoom_rects:

                rect.set_stroke(GOLD_A, 3)

                self.play(Create(rect), run_time=0.3)

                self.play(
                    self.camera.frame.animate
                    .move_to(rect.get_center())
                    .set(width=rect.width).set(height=rect.height),  
                    run_time=1,
                    rate_func=smooth
                )

                self.wait(wait_list[index_time])
                index_time+=1

                self.play(FadeOut(rect))

            self.play(
                Restore(self.camera.frame),
                run_time=1,
                rate_func=smooth
            )

            self.wait(1)

            self.play(
                FadeOut(img), 
                # FadeOut(title),
            )
            self.play(
                FadeOut(bg_rect,run_time=0.5),
            )

        items_list = [  "The Birth of Norms", 
                        "From Norms to Metrics", 
                        r"Cauchy Sequences \\ The Mystery of Nearness", 
                        "Banach Spaces",  ] # \\ The Kingdom of Completeness

        selected_title = Tex(items_list[topic_number], color=BLACK, font_size=80)
        selected_title.move_to(title.get_center())
        
        return selected_title

    def scene2(self,):
        warning_text = MathTex(
            r"X \text{ is a vector space over } \mathbb{K},",
            r"\text{where } \mathbb{K} \text{ is } \mathbb{R} \text{ or } \mathbb{C}.",
            color=BLACK,
        )
        bg_rect = Rectangle(
            width=config.frame_width, 
            height=config.frame_height, 
            stroke_width=0, 
            fill_color=light_red, 
            fill_opacity=0.2
        )
        self.add(bg_rect)
        self.play(
            FadeIn(bg_rect, run_time=0.5),
        )
        self.show_warning(warning_text,True)
        self.play(
            FadeOut(bg_rect), 
        )
        self.wait(0.5)

    def scene1_SubScene1(self,):
        plane = NumberPlane(
            y_range=[-4, 7, 0.5],
            x_range=[-4, 7, 0.5],
            background_line_style={"stroke_color": axes_background_color, "stroke_opacity": 0.5},
            y_length=6,
            x_length=8,
        ).move_to([0, 0, 0]).shift(DOWN*2)
        # self.wait(0.5)

        # draw axes on top
        axes = Axes(  # NumberLine
            y_range=[-4, 5, 0.5],
            y_length=6,
            x_range=[-4, 7, 0.5],
            x_length=8,
            axis_config={"color": medium_blue, "include_ticks": False, "tip_length":0.25, "tip_shape":StealthTip} # "tip_shape":ArrowTip.TIP_STYLE_ROUND
        ).move_to([0, 0, 0]).shift(DOWN*2)
        # self.wait(0.5)

        # draw vector in (0,0) - a
        vector_a = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(5,3),
            buff=0,
            stroke_width=6,
            color=dark_green,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        # self.wait(0.5)

        # draw vector in (0,0) - b
        vector_b = Arrow(
            start=axes.c2p(0,0),
            end=axes.c2p(-3,5),
            buff=0,
            stroke_width=6,
            color=dark_red,
            tip_length=0.25,
            tip_shape=StealthTip
        )
        # self.wait(0.5)

        # add texts
        a_text = MathTex(r"\overrightarrow{a} = (a_1, a_2)",color=BLACK).move_to(vector_a.get_end()+0.5*RIGHT+0.5*UP)
        # self.wait(0.5)

        b_text = MathTex(r"\overrightarrow{b} = (b_1, b_2)",color=BLACK).move_to(vector_b.get_end()+0.5*LEFT+0.5*UP)
        # self.wait(0.5)

        inner_product_text = MathTex(" \\langle \\vec{a}, \\vec{b} \\rangle = a_1 b_1 + a_2 b_2 = 0 ",color=BLACK).move_to(plane.get_center() + 0.75*DOWN)
        # self.wait(0.5)

        self.play(
            Create(plane, run_time=0.2),
            Create(axes, run_time=0.2),
            GrowArrow(vector_a, run_time=0.3, rate_func=rush_from),
            FadeIn(a_text, shift=UP*0.2),
            GrowArrow(vector_b, run_time=0.3, rate_func=rush_from),
            FadeIn(b_text, shift=UP*0.2),
            FadeIn(inner_product_text, shift=UP*0.2),
        )

        self.wait(1)

        self.play(
            FadeOut(plane),
            FadeOut(axes),
            FadeOut(vector_a),
            FadeOut(vector_b),
            FadeOut(a_text),
            FadeOut(b_text),
            FadeOut(inner_product_text),
        )


    def scene1(self,):
        """scene 1: title screen"""

        style = {
            "font_size": 85, "color": BLACK
        }

        title_up = Tex('Kinds of', 'Orthogonality',arg_separator=" ",**style).to_edge(UP)
        title_up[1].set_color(GREEN_E)
        title_down = Tex('in', 'Banach Spaces',arg_separator=" ",**style).move_to(title_up.get_center()+DOWN*0.75)
        title_down[1].set_color(GREEN_E)
        title_part = MathTex('part','\\text{ 1}',color=BLACK, font_size=70).move_to(title_down.get_center() + 0.75*DOWN)
        
        
        # 1-2 : add image

        star1 = ImageMobject("images/star_1_img.png").move_to(title_up.get_center()+ 6*LEFT + 0.5*DOWN )
        self.add(star1)

        star2 = ImageMobject("images/star_1_img.png").move_to(title_down.get_center()+ 5*RIGHT + 1.5*DOWN )
        self.add(star2)

        self.play(
            Write(title_up),
            Write(title_down),
            Write(title_part),
        )

        # 1-3 : add shapes

        # draw axes on top
        self.scene1_SubScene1()

        self.wait(1)

        self.play(
            Unwrite(title_up),
            Unwrite(title_down),
            Unwrite(title_part),
        )

        self.remove(star1)
        self.remove(star2)